from random import uniform
from pprint import pprint


file = open('file2.txt')


def init_array():
    try:
        line = file.readline().split(' ')
        values = [int(el) for el in line]
        print(values)
        return values
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def negative_numbers_multiplication(array):
    try:
        negative_values = [num for num in array if num < 0]
        negative_result = 1
        for num in negative_values:
            negative_result *= num
        print("Negative nums multiplication: " + str(negative_result))
        return negative_result
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def before_max_summary(array):
    try:
        max_index = array.index(max(array))
        print("Max: " + str(array[max_index]) + '\n' + "Index: " + str(max_index))
        before_max_el = []
        result = 0
        for i in range(0, max_index):
            if array[i] >= 0:
                result += array[i]
        print('Positive nums sum before max: ' + str(result))
        return result
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


if __name__ == '__main__':
    try:
        arr = init_array()
        negative_numbers_multiplication(arr)
        before_max_summary(arr)
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)
