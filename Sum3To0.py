def sum_to_target_3(nums):
    result_set = []
    for i in range(0, len(nums) - 2):
        sol_set = []
        remainder = 0 - nums[i]

        for j in range(i+1, len(nums)):
            if sol_set.__contains__(remainder - nums[j]):
                result_set.append([nums[i], nums[j], remainder - nums[j]])
            else:
                sol_set.append(nums[j])

    return list(set([tuple(t) for t in result_set]))


print(sum_to_target_3([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))