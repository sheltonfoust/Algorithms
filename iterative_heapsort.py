from test import *

def shift_down(arr, length, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < length and arr[left] > arr[largest]:
            largest = left
        if right < length and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

def heap_sort(arr):      
    for i in range(len(arr) // 2 - 1, -1, -1):
        shift_down(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        shift_down(arr, i, 0)

print(test_sort(heap_sort, True))