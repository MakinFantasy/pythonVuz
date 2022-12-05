file = open('file2.txt')


def first():
    values_str = file.readline().split(' ')
    values = []
    for i in values_str:
        values.append(int(i))
    print(values)


def sec():
    values_str = file.readline().split(' ')
    values = []
    for i in values_str:
        values.append(int(i))
    print(values)


first()
sec()
