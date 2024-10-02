from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((prob, v))
            graph[v].append((prob, u))
        
        probability = {i: 0 for i in range(n)}
        probability[start_node] = 1

        pq = [(-1, start_node)]

        while pq:
            cur_prob, cur_v = heapq.heappop(pq)
            cur_prob = -cur_prob

            if cur_v == end_node:
                return cur_prob

            for prob, next_v in graph[cur_v]:
                next_prob = cur_prob * prob
                if next_prob > probability[next_v]:
                    probability[next_v] = next_prob
                    heapq.heappush(pq, (-next_prob, next_v))
        
        return 0