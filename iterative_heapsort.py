from test import *
def sift_down(arr, parent, end): # end is exclusive
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
        sift_down(arr, i, len(arr))

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        sift_down(arr, 0, i)

print(test_sort(heapsort, True))