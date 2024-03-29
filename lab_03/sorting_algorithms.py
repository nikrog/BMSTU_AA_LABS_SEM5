# Артюхин Николай ЛР3 (Сортировки)
from functools import reduce


# Гномья сортировка
# Обход элементов ведется от начала массива до его конца, сравниваются соседние элементы.
# Если два соседних элемента пришлось поменять местами,
# то делается шаг назад на 1 элемент.
def gnome_sort(arr):
    i = 1
    n = len(arr)
    #c = 0
    while i < n:
        #c += 1
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
        else:
            i += 1
    #print(c)
    return arr


# Подсчет количества цифр в числе
def count_digits(num):
    c = 0
    num = abs(num)
    while num > 0:
        num //= 10
        c += 1
    return c


# Считаем количество цифр в максимальном числе из массива
def num_digits(arr):
    max_num = abs(arr[0])
    n = len(arr)
    for i in range(n):
        if max_num < abs(arr[i]):
            max_num = abs(arr[i])
    return count_digits(max_num)


# Поразрядная сортировка (по младшим разрядам - LSD)
# Сравнение производится поразрядно: сначала сравниваются значения одного крайнего разряда,
# и элементы группируются по результатам этого сравнения, затем сравниваются значения следующего разряда, соседнего,
# и элементы либо упорядочиваются по результатам сравнения значений этого разряда внутри образованных
# на предыдущем проходе групп, либо переупорядочиваются в целом, но сохраняя относительный порядок,
# достигнутый при предыдущей сортировке.
# Затем аналогично делается для следующего разряда, и так до конца.
def radix_sort(arr):
    m_dig = num_digits(arr)
    #print(m_dig)
    for d in range(0, m_dig):
        # 19, т.к существует всего 10 возможных цифр [0...9],
        # для отрицательных чисел введем дополнительные цифры [-9...-1]
        tmp = [[] for i in range(19)]
        for i in range(len(arr)):
            if arr[i] < 0:
                num = -((abs(arr[i]) // (10 ** d)) % 10)
            else:
                num = (arr[i] // (10 ** d)) % 10
            tmp[9 + num].append(arr[i])
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


if __name__ == '__main__':
    while True:
        n_a = int(input("Введите количество элементов в массиве: "))
        print(f"Введите {n_a} элементов массива: ")
        a = list(map(int, input().split(maxsplit=n_a)))
        print("Исходный массив: ", a)
        a_copy = a
        print("Гномья сортировка: ", gnome_sort(a_copy))
        a_copy = a
        print("Сортировка выбором: ", selection_sort(a_copy))
        a_copy = a
        print("Поразрядная сортировка: ", radix_sort(a_copy))
        cmd = str(input("Продожить - <ENTER>, выйти - q >> "))
        if cmd == 'q':
            exit()