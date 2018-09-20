def maxSubArraySum(nums):
    curr_max = curr_global = nums[0]

    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        if curr_max > curr_global:
            curr_global = curr_max

    return curr_global


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArraySum(nums))