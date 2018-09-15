def removeDups(nums):
    #[1,1,2]
    i = 0
    l = len(nums)

    for j in range(1, l):
        if nums[i] != nums[j]:
            i = i + 1
            nums[i] = nums[j]
    return nums[:i+1]


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDups(nums))
