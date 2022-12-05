file = open('file1.txt')

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
                print(str(a) + ": " + 'ОДЗ!!!')
            else:
                z = (((1 + a + a ** 2) / (2*a + a**2)) + 2 - ((1-a+a**2)/(2*a-a**2))) * (5 - 2*a**2)
                print(str(a) + ": " + str(z))
        print('Вычисления для первой формулы завершены\n')
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
            else:
                z = (4 - a**2) / 2
                print(str(a) + ": " + str(z))
        print('Выяисления для второй формулы завершены: ')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


try:
    z1()
    z2()
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
