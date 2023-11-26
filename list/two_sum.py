# two pointer 이용 O(nlogn)
def two_sum(nums, target):
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


print(two_sum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
print(two_sum(nums=[3, 2, 4], target=6))  # [1, 2]
print(two_sum(nums=[3, 3], target=6))  # [0, 1]
