# Артюхин Николай ИУ7-51Б ЛР1

import string
import random
from time import process_time

INF = -1


# DONE: Нерекурсивный (итерационный) алгоритм поиска расстояния Левенштейна
def lowenstein_dist_non_recursive(s1, s2, flag=False):
    # len of string + 1 empty symbol
    n = len(s1) + 1
    m = len(s2) + 1

    matrix = [[0 for i in range(m)] for j in range(n)]

    # trivial cases
    for j in range(1, m):
        matrix[0][j] = j  # INSERT
    for i in range(1, n):
        matrix[i][0] = i  # DELETE

    # filling the rest part of the matrix
    for i in range(1, n):
        for j in range(1, m):
            insert = matrix[i][j - 1] + 1
            delete = matrix[i - 1][j] + 1
            tmp = 1  # REPLACE
            if s1[i - 1] == s2[j - 1]:
                tmp = 0  # MATCH
            replace = matrix[i - 1][j - 1] + tmp
            matrix[i][j] = min(insert, delete, replace)

    if flag:
        print('Матрица:')
        for row in matrix:
            print(row)

    return matrix[n - 1][m - 1]  # Result


# DONE: Нерекурсивный (итерационный) алгоритм поиска расстояния Дамерау-Левенштейна
def damerau_lowenstein_dist_non_recursive(s1, s2, flag=False):
    # len of string + 1 empty symbol
    n = len(s1) + 1
    m = len(s2) + 1

    matrix = [[0 for i in range(m)] for j in range(n)]

    # trivial cases
    for j in range(1, m):
        matrix[0][j] = j  # INSERT
    for i in range(1, n):
        matrix[i][0] = i  # DELETE

    # filling the rest part of the matrix
    for i in range(1, n):
        for j in range(1, m):
            insert = matrix[i][j - 1] + 1
            delete = matrix[i - 1][j] + 1
            tmp = 1  # REPLACE
            if s1[i - 1] == s2[j - 1]:
                tmp = 0  # MATCH
            replace = matrix[i - 1][j - 1] + tmp
            matrix[i][j] = min(insert, delete, replace)
            # i -> i-1, i-1 -> i-2 because string don't have zero symbol in begin
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                exchange = matrix[i - 2][j - 2] + 1  # EXCHANGE
                matrix[i][j] = min(matrix[i][j], exchange)

    if flag:
        print('Матрица:')
        for row in matrix:
            print(row)

    return matrix[n - 1][m - 1]  # Result


# DONE: Дамерау-Левенштейна, рекурсивный без кеша
def damerau_lowenstein_dist_recursive(s1, s2):
    # trivial cases (exit)
    if not s1:
        return len(s2)
    elif not s2:
        return len(s1)

    insert = damerau_lowenstein_dist_recursive(s1, s2[:-1]) + 1
    delete = damerau_lowenstein_dist_recursive(s1[:-1], s2) + 1
    replace = damerau_lowenstein_dist_recursive(s1[:-1], s2[:-1]) + int(s1[-1] != s2[-1])

    if len(s1) > 1 and len(s2) > 1 and s1[-1] == s2[-2] and s1[-2] == s2[-1]:
        exchange = damerau_lowenstein_dist_recursive(s1[:-2], s2[:-2]) + 1
        return min(insert, delete, replace, exchange)
    else:
        return min(insert, delete, replace)

# вспомогательная функция
def damerau_lowenstein_dist_recursive_cache_helper(s1, s2, matrix):
    # len of string
    len1 = len(s1)
    len2 = len(s2)

    # trivial cases
    if not len1:
        matrix[len1][len2] = len2
    elif not len2:
        matrix[len1][len2] = len1
    else:
        # insert
        if matrix[len1][len2 - 1] == INF:
            damerau_lowenstein_dist_recursive_cache_helper(s1, s2[:-1], matrix)
        # delete
        if matrix[len1 - 1][len2] == INF:
            damerau_lowenstein_dist_recursive_cache_helper(s1[:-1], s2, matrix)
        # replace
        if matrix[len1 - 1][len2 - 1] == INF:
            damerau_lowenstein_dist_recursive_cache_helper(s1[:-1], s2[:-1], matrix)
        # exchange
        #if matrix[len1 - 2][len2 - 2] == INF:
            #damerau_lowenstein_dist_recursive_cache_helper(s1[:-2], s2[:-2], matrix)

        matrix[len1][len2] = min(matrix[len1][len2 - 1] + 1,
                                 matrix[len1 - 1][len2] + 1,
                                 matrix[len1 - 1][len2 - 1] + int(s1[-1] != s2[-1]))

        if len1 > 1 and len2 > 1 and s1[-1] == s2[-2] and s1[-2] == s2[-1]:
            matrix[len1][len2] = min(matrix[len1][len2],
                                     matrix[len1 - 2][len2 - 2] + 1)

        return

# DONE: Дамерау-Левенштейна, рекурсивный с кешем (матрицей)
def damerau_lowenstein_dist_recursive_cache(s1, s2, flag=False):
    # len of string + 1 empty symbol
    n = len(s1) + 1
    m = len(s2) + 1
    matrix = [[-1 for i in range(m)] for j in range(n)]
    damerau_lowenstein_dist_recursive_cache_helper(s1, s2, matrix)

    if flag:
        print('Матрица:')
        for row in matrix:
            print(row)

    return matrix[n - 1][m - 1]


def ask_user():
    str1 = input('Введите 1-ую строку: ')

    if str1 == '\q':
        exit()

    str2 = input('Введите 2-ую строку: ')

    print('\nРасстояние Левенштейна, нерекурсивный метод.')
    result = lowenstein_dist_non_recursive(str1, str2, True)
    print(f'Ответ: {result}')

    print('\nРасстояние Дамерау-Левенштейна, нерекурсивный метод.')
    result = damerau_lowenstein_dist_non_recursive(str1, str2, True)
    print(f'Ответ: {result}')

    print('\nРасстояние Дамерау-Левенштейна, рекурсивный без кеша.')
    result = damerau_lowenstein_dist_recursive(str1, str2)
    print(f'Ответ: {result}')

    print('\nРасстояние Дамерау-Левенштейна, рекурсивный с кешем (матрицей).')
    result = damerau_lowenstein_dist_recursive_cache(str1, str2, True)
    print(f'Ответ: {result}')

    print()

if __name__ == '__main__':
    while True:
        ask_user()
