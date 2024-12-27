from testsort import *


def quicksort(arr):
    quicksort_rec(arr, 0, len(arr) - 1)

def quicksort_rec(arr, start, end):
    if start >= end:
        return
    l = start
    for r in range(start, end):
        if arr[r] < arr[end]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    arr[l], arr[end] = arr[end], arr[l]
    quicksort_rec(arr, start, l - 1)
    quicksort_rec(arr, l + 1, end)




print(testsort(quicksort, True))
