from typing import List
def moveZeroes(nums: List[int]) -> None:
    left = 0

    for right in range(len(nums)):
        if nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums

print(moveZeroes([0,1,0,3,12]))