from test import *
def shift_down(arr, end, parent): # end is exclusive
    while True:
        left = 2 * parent + 1
        right = 2 * parent + 2
        
        largest = parent
        if left < end and arr[left] > arr[largest]:
            largest = left
        if right < end and arr[right] > arr[largest]:
            largest = right
        if largest == parent:
            break

        arr[parent], arr[largest] = arr[largest], arr[parent]
        parent = largest

def heapsort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        shift_down(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        shift_down(arr, i, 0)

print(test_sort(heapsort, True))