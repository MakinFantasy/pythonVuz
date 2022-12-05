# Var. 8

from math import sin, cos, pi, sqrt


def z1():
    print('First exp. test started')
    counter = 0
    while counter < 5:
        a = float(input())
        z = cos(a) + sin(a) + cos(3 * a) + sin(3 * a)
        print(z)
        counter += 1
    print('First exp. test finished')


def z2():
    print('Second exp. test started')
    counter = 0
    while counter < 5:
        a = float(input())
        z = 2 * sqrt(2) * cos(a) * sin((pi/4) + 2 * a)
        print(z)
        counter += 1
    print('Second exp. test finished')


if __name__ == '__main__':
    z1()
    z2()

