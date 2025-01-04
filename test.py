import random

def generate_random_array():
    array = []
    length = random.randint(0,20)
    for i in range(length):
        if random.randint(0, 3):
            array.append(random.randint(0, 100))
        elif array:
            array.append(array[random.randint(0, len(array) - 1)])
    return array



def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

def test_sort(sort_method, print_array = False):
    for foo in range(100):
        array = generate_random_array()
        length = len(array)
        sort_method(array)
        if print_array:
            print(array)
        if not is_sorted(array) or len(array) != length:
            return False
        
    return True

def is_kth_smallest(array, num, k):
    num_smaller = 0
    num_equal = 0
    for n in array:
        if n == num:
            num_equal += 1
        elif n < num:
            num_smaller += 1
    return num_smaller <= k and num_smaller + num_equal >= k

def test_select(select_method, print_info = False):
    for foo in range(100):
        array = generate_random_array()
        k = random.randint(0, len(array) - 1) if len(array) - 1 > 0 else 0
        kth_smallest = select_method(array, k)
        if print_info:
            print(k, " smallest :", kth_smallest, " in ", array)
        if not is_kth_smallest(array, kth_smallest, k):
            return False
    return True
        