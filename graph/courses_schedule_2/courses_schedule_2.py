from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        indegree = [0] * numCourses

        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([node for node in range(numCourses) if indegree[node] == 0])
        sorted_nodes = []

        while queue:
            cur_node = queue.popleft()
            sorted_nodes.append(cur_node)

            for connected_node in graph[cur_node]:
                indegree[connected_node] -= 1

                if indegree[connected_node] == 0:
                    queue.append(connected_node)

        return sorted_nodes if len(sorted_nodes) == numCourses else []