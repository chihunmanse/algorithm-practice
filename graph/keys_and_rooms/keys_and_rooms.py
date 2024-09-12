from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        queue = deque([0])

        while queue:
            cur_room = queue.popleft()
            visited[cur_room] = True
            for room in rooms[cur_room]:
                if not visited[room]:
                    visited[room] = True
                    queue.append(room)

        return all(visited)
