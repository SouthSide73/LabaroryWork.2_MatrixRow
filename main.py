import numpy as np
from numpy import linalg

try:
    m = int(input('Введите размерность квадратной матрицы:'))
    a = np.random.randint(15, size=(m, m))
    r = np.linalg.matrix_rank(a)
    print("Матрица:\n", a)
    print("Ранг матрицы:", r)
    t = int(input('Введите количество знаков после запятой в результате вычисления:'))
    t = 0.1 ** t
    n = 1
    first = 1
    second = 1
    fact = 1
    summa = 0
    fg = 1
    out = 1
    while abs(out) > t:
        out = 0
        fact = fact*(2*n - 1)*first*second
        fg += summa
        summa += (np.linalg.det(linalg.matrix_power(a, 2*n-1))) / fact
        out = abs(fg/summa)
        n += 1
        second = second * 2
        print(n-1, ':', summa, ' ', out)
    print('Сумма знакопеременного ряда:', summa)
except OverflowError:
    print("\nПрограмма не может произвести дальнейшие вычисления")
