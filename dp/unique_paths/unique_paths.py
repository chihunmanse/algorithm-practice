class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[-1] * n for _ in range(m)]
        
        for row in range(m):
            table[row][0] = 1
        
        for col in range(n):
            table[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                table[row][col] = table[row - 1][col] + table[row][col - 1]

        return table[m - 1][n - 1]