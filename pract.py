
def quicksort(arr, start, end):
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

quicksort([1, 32, 3, 3,4, 4, 4, 4], 0, 8 - 1)