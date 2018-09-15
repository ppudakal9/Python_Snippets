#Note: Please solve it without division and in O(n).
def productExceptSelf(nums):

    value = 1
    length = len(nums)
    product = [0] * length

    for i in range(0, length):
        product[i] = value
        value = value * nums[i]

    print(product)
    value = 1
    for i in range(length - 1, -1, -1):
        product[i] = product[i] * value
        value = value * nums[i]

    return product


print(productExceptSelf([1,2,3,4]))