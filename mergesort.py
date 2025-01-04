from test import *


def mergesort_wrap(arr):
    sorted_arr = mergesort(arr)
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    left = mergesort(arr[:m])
    right = mergesort(arr[m:])
    
    res = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    while l < len(left):
        res.append(left[l])
        l += 1
    while r < len(right):
        res.append(right[r])
        r += 1
    return res

print(test_sort(mergesort_wrap, True))