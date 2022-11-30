from math import *

try:
    R = float(input("Enter radius: "))
    X = float(input("Enter X: "))
    Y = float(input("Enter Y: "))
except Exception as e:
    print(e.__doc__)
    exit(1)



try:
    print('start')
    if ( (-2*R <= X <= 0) and (-2 * R <=  Y <= 0) and (Y >= -X - 2*R)) \
        or ( (0 <= Y <= 2 * R) and (0 <= X <= 2 * R) and (X**2 + Y**2 >= R ** 2)):
        print('Попал')
    else:
        print('Не попал')
except Exception as e:
    print(e)
    exit(1)
