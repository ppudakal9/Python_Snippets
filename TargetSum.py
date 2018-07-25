# recursive function to store and return sum
def rec_sum(nums_arr, target_sum, i, sum_cache):
    key = str(target_sum) + ':' + str(i)
    return_sum = 0
    if key in sum_cache:
        return sum_cache[key]

    if target_sum == 0:
        return 1
    elif target_sum < 0:
        return 0
    elif i < 0:
        return 0
    elif target_sum < nums_arr[i]:
        return_sum = rec_sum(nums_arr, target_sum, i - 1, sum_cache)
    else:
        return_sum = rec_sum(nums_arr, target_sum - nums_arr[i], i - 1, sum_cache) + rec_sum(nums_arr, target_sum,
                                                                                             i - 1, sum_cache)
    sum_cache[key] = return_sum
    return return_sum


# function to count number of elements required to add up to a given target number using memoization
def add_to_target(nums1, target1):
    sum_cache = {}
    i = len(nums1) - 1
    return rec_sum(nums1, target1, i, sum_cache)


nums = [2, 4, 6, 10]
target = 16
print(add_to_target(nums, target))
