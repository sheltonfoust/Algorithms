from test import *

def quickselect(arr, k):
    start, end = 0, len(arr) - 1
    if k < start or k > end:
        return None
    while True:
        l = start
        for r in range(start, end):
            if arr[r] < arr[end]:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
        arr[l], arr[end] = arr[end], arr[l]
        if l == k:
            return arr[k]
        elif l < k:
            start = l + 1
        else:
            end = l - 1

print(test_select(quickselect, True))