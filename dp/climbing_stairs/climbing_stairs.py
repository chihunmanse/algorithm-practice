class Solution:
    # bottom-up
    def climbStairs(self, n: int) -> int:
        table = [-1] * (n + 1)
        table[0] = 1
        table[1] = 1

        for i in range (2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        
        return table[n]

    # top-down
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def dp(n):
            if n == 0 or n == 1:
                return 1
            
            if memo[n] == -1:
                memo[n] = dp(n - 1) + dp(n - 2)
            
            return memo[n]
        
        return dp(n)
