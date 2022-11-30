from math import *

CONST_RADIUS = 2

try:
    x = float(input("Enter x: "))
    if x <= -1:
        y = -x - 1
    elif -1 < x <= 1:
        y = 0
    elif 1 < x <= 5:
        y = sqrt(CONST_RADIUS**2 - (x-3)**2)
    elif 5 < x:
        y = -0.5 * x + 2.5
except Exception as e:
    print(e.__doc__)
    exit(1)
print("x: {:6.2f} y:{:6.2f}".format(x, y))