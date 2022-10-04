# Артюхин Николай ЛР3 (Сортировки)
from functools import reduce


# Гномья сортировка
# Обход элементов ведется от начала массива до его конца, сравниваются соседние элементы.
# Если два соседних элемента пришлось поменять местами,
# то делается шаг назад на 1 элемент.
def gnome_sort(arr):
    i = 1
    n = len(arr)
    while i < n:
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
        else:
            i += 1
    return arr


# Гномья сортировка с оптимизацией
# запоминние позиции, с которой начались обмены,
# то затем можно сразу же перепрыгнуть в эту позицию,
# когда обмены завершены.
def gnome_sort_optimized(arr):
    i = 1
    j = 2
    n = len(arr)
    while i < n:
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
        else:
            i = j
            j += 1
    return arr

# Подсчет количества цифр в числе
def count_digits(num):
    c = 0
    while abs(num) > 0:
        num /= 10
        c += 1
    return c


# Считаем количество цифр в максимальном числе из массива
def num_digits(arr):
    max_num = arr[0]
    n = len(arr)
    for i in range(n):
        if max_num < arr[i]:
            max_num = arr[i]
    return count_digits(max_num)


# Поразрядная сортировка (по младшим разрядам - LSD)
def radix_sort(arr):
    m_dig = num_digits(arr)
    for d in range(0, m_dig):
        tmp = [[] for i in range(10)]
        for i in range(len(arr)):
            num = (arr[i] // (10 ** d)) % 10
            tmp[num].append(arr[i])
        arr = reduce(lambda x, y: x + y, tmp)
        #print(arr, tmp)
    return arr


# Сортировка выбором
# Проходим по массиву в поисках максимального элемента.
# Найденный максимум меняем местами с последним элементом.
# Неотсортированная часть массива уменьшилась на один элемент
# (не включает последний элемент, куда мы переставили найденный максимум).
# К этой неотсортированной части применяем те же действия, то есть
# находим максимум и ставим его на последнее место в неотсортированной части массива.
# И так продолжаем до тех пор, пока неотсортированная часть массива не уменьшится до одного элемента.
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        i_max = i
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i_max]:
                i_max = j
        if i_max != i:
            arr[i], arr[i_max] = arr[i_max], arr[i]
    return arr


def selection_sort2(arr):
    i = 1
    i_max = 0
    n = len(arr)
    while i < n:
        if arr[i] > arr[i_max]:
            i_max = i
        if i == n - 1:
            if arr[i_max] > arr[n - 1]:
                arr[n - 1], arr[i_max] = arr[i_max], arr[n - 1]
            n -= 1
            i = 0
            i_max = 0
        i += 1
    return arr



if __name__ == '__main__' :
    print(radix_sort([4, 9, -657, 10, 1, -67]))