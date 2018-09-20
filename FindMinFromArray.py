#will work for both sorted or unsorted array
def findMin(nums):
    minimum = nums[0]
    for i in nums:
        if minimum > i:
            minimum = i

    return minimum

#will work for a sorted array which has been rotated
def binarySearch(nums):
    if len(nums) == 1:
        return nums[0]

    #initialize left and right pointers
    left = 0
    right = len(nums) - 1

    #if first element is smaller than the last element in the array then there has been no rotation and we can return the first element as the
    #minimum element in the array
    if nums[left] < nums[right]:
        return nums[left]


    #perform modified binary search
    while right >= left:
        mid = left + (right - left) // 2

        # if middle element is greater than the element after it (mid + 1) that means we have found the minimum element at mid + 1 index
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # if middle element is less than the element before it (mid - 1) that means middle element is the minimum element
        if nums[mid] < nums [mid - 1]:
            return nums[mid]

        # if middle element is greater than the first element that means we need to look in the right half of the array
        if nums[mid] > nums[0]:
            left = mid + 1
        # if middle element is less than the first element that means we need to look in the left half of the array
        elif nums[mid] < nums[0]:
            right = mid - 1





nums = [-2,-5,13,-4444,99999,1]
print(findMin(nums))

nums = [4, 5, 6, 7, 2, 3]
print("Min Using binary Search in O(logN) = ", binarySearch(nums))
print("Min Using linear search in O(N) = ", findMin(nums))
