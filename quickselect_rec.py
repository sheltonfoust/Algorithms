from test import *
# Average Case 
# O(n) time
# O(logn)? space?


def quickselect_wrap(arr, k):
    return quickselect(arr, k, 0, len(arr) - 1)

def quickselect(arr, k, start, end):
    if k > end:
        return None
    l = start
    for r in range(start, end):
        if arr[r] < arr[end]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    arr[l], arr[end] = arr[end], arr[l]
    if l == k:
        return arr[k]
    elif l < k:
        return quickselect(arr, k, l + 1, end)
    else:
        return quickselect(arr, k, start, l - 1)
    
print(test_select(quickselect_wrap, True))