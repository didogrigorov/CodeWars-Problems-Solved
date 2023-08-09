def pipe_fix(nums):
    result = []
    for i in range(nums[0], nums[-1] + 1):
        result.append(i)

    return result


print(pipe_fix([6,9]))