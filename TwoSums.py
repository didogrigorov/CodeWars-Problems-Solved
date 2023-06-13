def twoSum(nums, target):
    checked_nums = {}

    for i in range(len(nums)):
        addition = target - nums[i]
        if addition in checked_nums:
            return [checked_nums[addition], i]

        checked_nums[nums[i]] = i

print(twoSum([1,2,3,4,5], 4))