from testsort import *


def mergesort(arr):
    sorted_arr = mergesort_rec(arr)
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

def mergesort_rec(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    left = mergesort_rec(arr[:m])
    right = mergesort_rec(arr[m:])
    
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

print(testsort(mergesort, True))