class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for i, num in enumerate(nums):
            key_num = target - num

            if key_num in dic:
                return [i, dic[key_num]]
            else:
                dic[num] = i

        return None 

    # two pointer 이용 O(nlogn)
    def twoSum(nums, target):
        nums = [[n, i] for i, n in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        l, r = 0, len(nums) - 1

        while l < r:
            num_sum = nums[l][0] + nums[r][0]
            if num_sum == target:
                return [nums[l][1], nums[r][1]]
            elif num_sum > target:
                r -= 1
            else:
                l += 1