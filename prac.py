from test import *
def shift_down(arr, end, parent): # end is exclusive
    while True:
        left = parent * 2 + 1
        right = parent * 2 + 2

        largest = parent
        if left < end and arr[left] > arr[largest]:
            largest = left
        if right < end and arr[right] > arr[largest]:
            largest = right
        if largest == parent:
            break

        arr[largest], arr[parent] = arr[parent], arr[largest]
        parent = largest

def heapsort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        shift_down(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        shift_down(arr, i, 0)

print(test_sort(heapsort, True))