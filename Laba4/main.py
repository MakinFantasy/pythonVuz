from random import uniform
from pprint import pprint


def init_array(length):
    array = []
    try:
        for i in range(length):
            array.append(uniform(-10, 10))
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)
    return array


def negative_numbers_multiplication(array):
    try:
        negative_numbers = [i for i in array if i < 0]
        negative_result = 1
        for num in negative_numbers:
            negative_result *= num
        return negative_result
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def before_max_summary(array):
    try:
        max_el = array.index(max(array))
        before_max_el = []
        for i in range(0, max_el):
            if array[i] >= 0:
                before_max_el.append(array[i])
        return sum(before_max_el)
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


if __name__ == '__main__':
    try:
        LENGTH = int(input('Input array lenght: '))
        userNums = init_array(LENGTH)
        pprint(userNums)
        print("Произведение отрицательных элементов: " + str(negative_numbers_multiplication(userNums)))
        print("Сумма положительных эл-ов, расположенных до максимального: " + str(before_max_summary(userNums)))
        userNums.reverse()
        print(userNums)
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)
