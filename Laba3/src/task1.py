from math import *


def initParams():
    CONST_RADIUS = 2
    X_START = float(input('Enter x start: '))
    X_END = float(input('Enter x end: '))
    X_DELTA = float(input('Enter dx: '))

def mainLine():
    print("+" + "-" * 8 + "+" + "-" * 8 + "+")


def columns():
    print('I   X    I    Y   I')


try:
    initParams()
    mainLine()
    columns()
    mainLine()

except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
