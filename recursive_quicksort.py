from test import *


def quicksort_wrap(arr):
    quicksort(arr, 0, len(arr) - 1)

def quicksort(arr, start, end): # end is inclusive
    if start >= end:
        return
    l = start
    for r in range(start, end):
        if arr[r] < arr[end]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    arr[l], arr[end] = arr[end], arr[l]
    quicksort(arr, start, l - 1)
    quicksort(arr, l + 1, end)




print(test_sort(quicksort_wrap, True))
