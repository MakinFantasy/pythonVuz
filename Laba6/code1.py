def z1(array):
    try:
        print('Вычесления для первой формулы: ')
        counter = 0
        while counter < 5:
            a = float(input('Введите значение а: '))
            if (1 + a + a**2 == 0) or (2*a + a**2 == 0) or (1-a+a**2 == 0) or (2*a-a**2 == 0):
                print('ОДЗ!!!')
                counter += 1
            else:
                z = (((1 + a + a ** 2) / (2*a + a**2)) + 2 - ((1-a+a**2)/(2*a-a**2))) * (5 - 2*a**2)
                print(z)
                counter += 1
        print('Вычисления для первой формулы завершены\n')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def z2():
    try:
        print('Выяисления для второй формулы: ')
        counter = 0
        while counter < 5:
            a = float(input('Введите значения а: '))
            if 4 - a**2 == 0:
                print('ОДЗ!!!')
                counter += 1
            else:
                z = (4 - a**2) / 2
                print(z)
                counter += 1
        print('Выяисления для второй формулы завершены: ')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


if __name__ == '__main__':
    try:
        file = open('file2.txt')
        text = file.readlines()
        nums = []
        for line in text:
            el = line.split(' ')
            for i in el:
                nums.append(i)
        z1()
        z2()
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)
