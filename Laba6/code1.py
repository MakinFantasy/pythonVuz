file = open('file1.txt')
res = open('res1.txt', 'a')


def clear_file():
    try:
        res.truncate(0)
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def clear_line():
    try:
        res.write('\n')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def z1():
    try:
        print('Вычесления для первой формулы: ')
        values_str = file.readline().split(' ')
        values = []
        for i in values_str:
            values.append(int(i))
        for i in values:
            a = i
            if (1 + a + a**2 == 0) or (2*a + a**2 == 0) or (1-a+a**2 == 0) or (2*a-a**2 == 0):
                print("Z1" + str(a) + ": " + 'ОДЗ!!!')
                res.write("Z1: " + str(a) + ": " + 'ОДЗ!!!' + '\n')
            else:
                z = (((1 + a + a ** 2) / (2*a + a**2)) + 2 - ((1-a+a**2)/(2*a-a**2))) * (5 - 2*a**2)
                print(str(a) + ": " + str(z))
                res.write("Z1: " + str(a) + ": " + str(z) + '\n')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def z2():
    try:
        print('Выяисления для второй формулы: ')
        values_str = file.readline().split(' ')
        values = []
        for i in values_str:
            values.append(int(i))
        for i in values:
            a = i
            if 4 - a**2 == 0:
                print(str(a) + ": " + 'ОДЗ!!!')
                res.write("Z2: " + str(a) + ": " + 'ОДЗ!!!' + '\n')
            else:
                z = (4 - a**2) / 2
                print(str(a) + ": " + str(z))
                res.write("Z2: " + str(a) + ": " + str(z) + '\n')

        print('Выяисления для второй формулы завершены: ')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


try:
    clear_file()
    z1()
    clear_line()
    z2()
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
