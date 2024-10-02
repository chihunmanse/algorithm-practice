from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    
    while queue:
        cur_node = queue.popleft()
        cur_distance = distances[cur_node]
        
        for next_node in graph[cur_node]:
            if distances[next_node] == -1:
                distances[next_node] = cur_distance + 1
                queue.append(next_node)
    
    return distances.count(max(distances))