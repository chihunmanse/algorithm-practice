from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]

        def bfs(row, col, grid):
            move_point = [[0,1], [1,0], [0, -1], [-1, 0]]
            visited[row][col] = True
            queue = deque([(row, col)])
            while queue:
                cur_row, cur_col = queue.popleft()
                for point in move_point:
                    next_row = cur_row + point[0]
                    next_col = cur_col + point[1]
                    if 0 <= next_row < row_len and 0 <= next_col < col_len:
                        if grid[next_row][next_col] == '1' and not visited[next_row][next_col]:
                            visited[next_row][next_col] = True
                            queue.append((next_row, next_col))
        
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j, grid)
                    count += 1
        
        return count



            