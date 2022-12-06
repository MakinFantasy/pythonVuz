from pprint import pprint


file = open('file3.txt')
res = open('res3.txt', 'a')


def clear_file():
    res.truncate(0)


def clear_line():
    res.write('\n')


def main():
    try:
        lines = file.readlines()
        matrix = []
        for line in lines:
            int_line = [int(num) for num in line.split(' ')]
            matrix.append(int_line)
            res.write(line)
        pprint(matrix)
        clear_line()
        clear_line()


        sum_arr = []
        for i in range(len(matrix)):
            sum = 0
            flag = True
            for el in matrix[i]:
                if el >= 0:
                    sum += el
                else:
                    flag = False
                    continue
            if flag:
                print("Sum " + str(i + 1) + ": " + str(sum) + '\n')
                sum_arr.append(sum)
                res.write("Sum " + str(i + 1) + ": " + str(sum)  + '\n')
            else:
                print("В строке " + str(i + 1) + " есть отрицательные элементы" + '\n')
                res.write("В строке " + str(i + 1) + " есть отрицательные элементы" + '\n')
        clear_line()
        final_sum = 0
        for i in sum_arr:
            final_sum += i
        print("Сумма всех строк без отрицательных элементов: ", str(final_sum) + '\n')
        res.write("Сумма всех строк без отрицательных элементов: " + str(final_sum)  + '\n')
        clear_line()


        n = len(matrix[0])
        countDiagonal = 2 * n - 3
        sumArray = 0
        minSum = 1000
        for i in range(countDiagonal):
            t = n - i - 1
            row = -t if t < 0 else 0
            col = t-1 if t > 0 else 0
            while row < n and col < n:
                sumArray += matrix[row][col]
                row += 1
                col += 1
            if minSum > sumArray:
                minSum = sumArray
            sumArray = 0

        print("Минимум, среди сумм диагоналей паралельных главной: " + str(minSum) + '\n')
        res.write("Минимум, среди сумм диагоналей паралельных главной: " + str(minSum)  + '\n')
        clear_line()

    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


try:
    clear_file()
    main()
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
