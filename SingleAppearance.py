def singleAppearance(nums):
    d = {}

    for i in range(0, len(nums)):
        if nums[i] in d:
            d[nums[i]] += 1
        else:
            d[nums[i]] = 1

    for k, v in d.items():
        if v == 1:
            print(k)
        else:
            continue


def xor_elements(nums):
    res = nums[0]

    for i in range(1, len(nums)):
        res = res ^ nums[i]

    return res


nums = [2, 3, 5, 4, 5, 3, 4]
singleAppearance(nums)

a = [15, 18, 16, 18, 16, 15, 89]
singleAppearance(a)

nums = [2, 3, 5, 4, 5, 3, 4]
print(xor_elements(nums))

a = [15, 18, 16, 18, 16, 15, 89]
print(xor_elements(a))