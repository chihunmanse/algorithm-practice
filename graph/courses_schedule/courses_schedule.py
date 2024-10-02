from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프
        graph = defaultdict(list)

        # 진입 차수 배열
        indegree = [0] * numCourses

        # 간선 정보를 기반으로 그래프 및 진입 차수 배열 초기화
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        # 진입 차수가 0인 노드들을 큐에 추가
        queue = deque([node for node in range(numCourses) if indegree[node] == 0])
        sorted_nodes = []

        while queue:
            cur_node = queue.popleft()
            sorted_nodes.append(cur_node)

            # 현재 노드에 연결된 노드들의 진입 차수를 감소
            for connected_node in graph[cur_node]:
                indegree[connected_node] -= 1

                # 진입 차수가 0이면 큐에 추가
                if indegree[connected_node] == 0:
                    queue.append(connected_node)

        # 정렬된 노드의 수가 전체 노드 수와 같지 않으면 순환이 존재 
        return len(sorted_nodes) == numCourses
