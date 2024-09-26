class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        table = [-1] * n

        table[0] = nums[0]

        for i in range(1, n):
            table[i] = nums[i] + max(0, table[i - 1])
        
        return max(table)
        