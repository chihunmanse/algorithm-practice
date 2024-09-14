from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        # 시작점이나 끝점이 막혀있는지 확인
        if grid[0][0] == 1 or grid[row_len - 1][col_len - 1] == 1:
            return -1

        # 8방향 이동을 위한 방향 설정
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # BFS 큐: 각 요소는 (row, col, distance) 튜플
        queue = deque([(0, 0, 1)])  # (0, 0)에서 시작하고, 거리는 1로 설정
        visited = [[False] * col_len for _ in range(row_len)]
        visited[0][0] = True

        while queue:
            cur_row, cur_col, cur_dist = queue.popleft()

            # 목표 위치(우하단)에 도달하면 거리 반환
            if cur_row == row_len - 1 and cur_col == col_len - 1:
                return cur_dist

            # 8방향 모두 탐색
            for dr, dc in directions:
                next_row = cur_row + dr
                next_col = cur_col + dc

                # 다음 위치가 경계 내에 있고, 방문하지 않았으며, 0(열린 길)인 경우
                if 0 <= next_row < row_len and 0 <= next_col < col_len and not visited[next_row][next_col] and grid[next_row][next_col] == 0:
                    queue.append((next_row, next_col, cur_dist + 1))
                    visited[next_row][next_col] = True

        # 경로를 찾지 못한 경우 -1 반환
        return -1
