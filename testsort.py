import random
def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

def testsort(sort_method, print_array = False):
    for k in range(100):
        array = []
        length = random.randint(0,20)
        for i in range(length):
            if random.randint(0, 3):
                array.append(random.randint(0, 100))
            elif array:
                array.append(array[random.randint(0, len(array) - 1)])
        length = len(array)
        sort_method(array)
        if not is_sorted(array):
            return False
        if len(array) != length:
            return False
        if print_array:
            print(array)
    return True