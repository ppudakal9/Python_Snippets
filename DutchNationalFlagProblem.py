def swap(arr_swap, x, y):
    temp = arr_swap[x]
    arr_swap[x] = arr_swap[y]
    arr_swap[y] = temp


def dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            swap(arr, mid, high)
            high -= 1

    return arr


print(dutch_national_flag([2,2,2,0,0,0,0,1,1]))