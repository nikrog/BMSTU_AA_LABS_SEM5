# Артюхин Николай ИУ7-51Б ЛР2 (Алгоритмы умножения матриц)

def input_matrix():
    n = int(input("Введите кол-во строк: "))
    m = int(input("Введите кол-во столбцов: "))
    matr = []
    for i in range(n):
        s = list(int(i) for i in input().split())
        if len(s) < m:
            print("Недостаточно данных для исходных матриц!")
            exit()
        matr.append(s)
    return matr


def print_matrix(matr):
    for i in range(len(matr)):
        print(matr[i])


# Стандартный алгоритм умножения матриц
def standart_mult_matr(matr1, matr2):
    if len(matr1[0]) != len(matr2):
        print("Некорректные размеры матриц для умножения!")
        exit()

    n = len(matr1)
    m = len(matr1[0])
    q = len(matr2[0])

    res = [[0] * q for i in range(n)]

    for i in range(n):
        for j in range(q):
            for k in range(m):
                res[i][j] = res[i][j] + matr1[i][k] * matr2[k][j]

    return res


# Алгоритм Винограда умножения матриц
def vinograd_mult_matr(matr1, matr2):
    if len(matr1[0]) != len(matr2):
        print("Некорректные размеры матриц для умножения!")
        exit()

    n = len(matr1)
    m = len(matr1[0])
    q = len(matr2[0])

    res = [[0] * q for i in range(n)]
    # векторы строк matr1
    mulh = [0] * n
    for i in range(n):
        for k in range(m // 2):
            mulh[i] = mulh[i] + matr1[i][2 * k] * matr1[i][2 * k + 1]

    # векторы столбцов matr2
    mulv = [0] * q
    for i in range(q):
        for k in range(m // 2):
            mulv[i] = mulv[i] + matr2[2 * k][i] * matr2[2 * k + 1][i]

    # заполнение матрицы res
    for i in range(n):
        for j in range(q):
            res[i][j] = - mulh[i] - mulv[j]
            for k in range(m // 2):
                res[i][j] = res[i][j] + (matr1[i][2 * k] + matr2[2 * k + 1][j]) * \
                            (matr1[i][2 * k + 1] + matr2[2 * k][j])

    if m % 2 == 1:
        for i in range(n):
            for j in range(q):
                res[i][j] = res[i][j] + matr1[i][m - 1] * matr2[m - 1][j]

    return res


# Оптимизированный алгоритм Винограда умножения матриц
def vinograd_optimized_mult_matr2(matr1, matr2):
    if len(matr1[0]) != len(matr2):
        print("Некорректные размеры матриц для умножения!")
        exit()

    n = len(matr1)
    m = len(matr1[0])
    q = len(matr2[0])

    res = [[0] * q for i in range(n)]

    # векторы строк matr1
    mulh = [0] * n
    for i in range(n):
        for k in range(m // 2):
            mulh[i] += matr1[i][k << 1] * matr1[i][(k << 1) + 1]

    # векторы столбцов matr2
    mulv = [0] * q
    for i in range(q):
        for k in range(m // 2):
            mulv[i] += matr2[k << 1][i] * matr2[(k << 1) + 1][i]

    flag = m % 2
    # заполнение матрицы res
    for i in range(n):
        for j in range(q):
            res[i][j] = - mulh[i] - mulv[j]
            for k in range(m // 2):
                res[i][j] += (matr1[i][k << 1] + matr2[(k << 1) + 1][j]) * \
                            (matr1[i][(k << 1) + 1] + matr2[k << 1][j])
            if flag == 1:
                res[i][j] += matr1[i][m - 1] * matr2[m - 1][j]
    return res


# Оптимизированный алгоритм Винограда умножения матриц
def vinograd_optimized_mult_matr(matr1, matr2):
    if len(matr1[0]) != len(matr2):
        print("Некорректные размеры матриц для умножения!")
        exit()

    n = len(matr1)
    m = len(matr1[0])
    q = len(matr2[0])

    res = [[0] * q for i in range(n)]

    # векторы строк matr1
    mulh = [0] * n
    for i in range(n):
        for k in range(1, m, 2):
            mulh[i] += matr1[i][k] * matr1[i][k - 1]

    # векторы столбцов matr2
    mulv = [0] * q
    for i in range(q):
        for k in range(1, m, 2):
            mulv[i] += matr2[k][i] * matr2[k - 1][i]

    flag = m % 2
    # заполнение матрицы res
    for i in range(n):
        for j in range(q):
            res[i][j] = - mulh[i] - mulv[j]
            for k in range(1, m, 2):
                res[i][j] += (matr1[i][k] + matr2[k - 1][j]) * \
                            (matr1[i][k - 1] + matr2[k][j])
            if flag == 1:
                res[i][j] += matr1[i][m - 1] * matr2[m - 1][j]
    return res


if __name__ == "__main__":
    print("Ввод матрицы A")
    a = input_matrix()

    print("Ввод матрицы B")
    b = input_matrix()

    print("Результат (стандартный алгоритм умножения матриц): ")
    res_s = standart_mult_matr(a, b)
    print_matrix(res_s)

    print("Результат (алгоритм Винограда умножения матриц): ")
    res_v = vinograd_mult_matr(a, b)
    print_matrix(res_v)

    print("Результат (оптимизированный алгоритм Винограда умножения матриц): ")
    res_ov = vinograd_optimized_mult_matr(a, b)
    print_matrix(res_ov)
