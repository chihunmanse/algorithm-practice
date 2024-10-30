class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0

        for x in nums:
            if x - 1 not in nums_set:
                target = x + 1
                value = 1

                while target in nums_set:
                    target += 1
                    value += 1
                
                result = max(result, value)


        return result