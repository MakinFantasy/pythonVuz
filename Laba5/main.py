import numpy as np

def main():
    try:
        n=int(input("Введите размер матрицы (NxN): "))


        A = np.random.randint(-3, 10, (n, n))
        for Row in range(n):
            for Col in range(n):
                print("{0:>5.0f}".format(A[Row][Col]), end=" ")
            print()
        print()
        

        # summ = 0
        # isNeg = False

        # for i in range(n):
        #     for j in range(n):
        #         if A[i][j] < 0:
        #             isNeg = True
        #             continue
        #         summ += A[i][j]
        #     if isNeg == False:
        #         print("Сумма элементов всех строк без отрицательного элемента: ", summ)
        #     sum = 0
        #     isNeg = False
            
        sum_arr = []
        for i in range(len(A)):
            sum = 0
            flag = True
            for el in A[i]: 
                if el >= 0:
                    sum += el
                else:
                    flag = False
                    continue
            if flag:
                print("Sum " + str(i + 1) + ": " + str(sum))
                sum_arr.append(sum)

            else:
                print("В строке есть отрицательные элементы")
        

        res = 0
        for i in sum_arr:
            res += i
        print("Сумма всех строк без отрицательных элементов: ", res)

        countDiagonal = 2 * n - 1
        sumArray = 0
        minSum = 1000
        for i in range(countDiagonal):
            t = n - i - 1
            row = -t if t < 0 else 0
            col = t if t > 0 else 0
            while row < n and col < n:
                sumArray += A[row][col]
                row += 1
                col += 1
            if minSum > sumArray:
                minSum = sumArray
            sumArray = 0

        print("Минимум, среди сумм диагоналей паралельных главной: ", minSum)
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


main()