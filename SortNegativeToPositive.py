def shiftArray(arr, currIndex, negIndex):
    temp = arr[currIndex]

    for j in range(currIndex, negIndex+1, -1):
        arr[j] = arr[j-1]

    arr[negIndex+1] = temp


def sort_neg_to_pos(arr):
    #initialize negIndex to -1. negIndex will keep track of last seen negative element
    negIndex = -1

    #if first element is negative set negIndex to 0
    if arr[0] < 0:
        negIndex = 0

    #loop from 1 till end of array
    for i in range(1, len(arr)):
        #check if current array element is less than or equal to 0 and also if the previous element is > 0. If yes, then shift the array
        # from negIndex+1 to current index i and increment negIndex by 1
        if arr[i] <= 0 and arr[i-1] > 0:
            shiftArray(arr, i, negIndex)
            negIndex += 1
    return arr


a = [-2, 4, -19, 4, 0]
print(sort_neg_to_pos(a))

a = [1, 7, -5, 9, -12, 15]
print(sort_neg_to_pos(a))