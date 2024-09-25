class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        table = [-1] * n
        
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])

        for i in range(2, n):
            table[i] = max(table[i - 1], table[i - 2] + nums[i])

        return table[n - 1]
      