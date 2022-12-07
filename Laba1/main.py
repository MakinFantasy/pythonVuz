# Var. 8

from math import sin, cos, pi, sqrt


def z1():
    try:
        print('First exp. test started')
        counter = 0
        while counter < 5:
            a = float(input())
            if (1 + a + a**2 == 0) or (2*a + a**2 == 0) or (1-a+a**2 == 0) or (2*a-a**2 == 0):
                print('ОДЗ!!!')
                counter += 1
            else:
                z = ( ( (1 + a + a**2) / (2*a + a**2))  + 2 - ( (1 - a + a**2) / (2*a - a**2) ) ) * (5 - 2*a**2)
                print("z(a)" + str(z))
            counter += 1
        print('First exp. test finished')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def z2():
    try:
        print('Second exp. test started')
        counter = 0
        while counter < 5:
            a = float(input())
            z = (4 - a**2) / 2
            print(z)
            counter += 1
        print('Second exp. test finished')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


if __name__ == '__main__':
    z1()
    z2()
