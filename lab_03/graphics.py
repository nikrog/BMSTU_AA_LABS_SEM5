# Артюхин Николай ЛР3 (Сортировки)
# Модуль замеров процессорного времени реализаций алгориттмов сортировки + построение графиков

from time import process_time
import random
import matplotlib.pyplot as plt

from sorting_algorithms import *


def get_best_array(n):
    array = []

    for i in range(n):
        array.append(i)

    return array


def get_worst_array(n):
    array = []

    for i in range(n):
        array.append(n - i)

    return array


def get_random_array(n):
    array = []

    for i in range(n):
        array.append(random.randint(0, 50000))

    return array


def get_proc_time(func, arr):
    t1 = process_time()
    func(arr)
    t2 = process_time() - t1

    return t2


def measure_time(get_array, n1, n2, step, n_it):
    t_gnome = []
    t_radix = []
    t_selection = []

    for n in range(n1, n2, step):
        t = 0

        for i in range(n_it):
            arr = get_array(n)
            t += get_proc_time(gnome_sort, arr)

        t_gnome.append(t / n_it * 1000000)  # из секунд в микросекунды
        t = 0

        for i in range(n_it):
            arr = get_array(n)
            t += get_proc_time(radix_sort, arr)

        t_radix.append(t / n_it * 1000000)  # из секунд в микросекунды
        t = 0

        for i in range(n_it):
            arr = get_array(n)
            t += get_proc_time(selection_sort, arr)

        t_selection.append(t / n_it * 1000000)  # из секунд в микросекунды

    return t_gnome, t_radix, t_selection


n1 = 100  # от
n2 = 1000  # до
step = 200  # шаг
n_iters = 100  # количество прогонов
res1 = measure_time(get_best_array, n1, n2 + 1, step, n_iters)
res2 = measure_time(get_worst_array, n1, n2 + 1, step, n_iters)
res3 = measure_time(get_random_array, n1, n2 + 1, step, n_iters)

len_arr = [100, 300, 500, 700, 900]  # длины массивов для прогонки
fig1 = plt.figure(figsize=(10, 7))
plot = fig1.add_subplot()
plot.plot(len_arr, res1[0], label="Гномья сортировка")
plot.plot(len_arr, res1[1], label="Поразрядная сортировка")
plot.plot(len_arr, res1[2], label="Сортировка выбором")
plt.legend()
plt.grid()
plt.title("Временные характеристики алгоритмов сортировки (лучший случай)")
plt.ylabel("Затраченное время (мкс)")
plt.xlabel("Длина массива")
print("Отсортированные данные (л.с.): ", res1)

fig2 = plt.figure(figsize=(10, 7))
plot = fig2.add_subplot()
plot.plot(len_arr, res2[0], label="Гномья сортировка")
plot.plot(len_arr, res2[1], label="Поразрядная сортировка")
plot.plot(len_arr, res2[2], label="Сортировка выбором")
plt.legend()
plt.grid()
plt.title("Временные характеристики алгоритмов сортировки (худший случай)")
plt.ylabel("Затраченное время (мкс)")
plt.xlabel("Длина массива")
print("Обратный порядок (х.с.): ", res2)

fig3 = plt.figure(figsize=(10, 7))
plot = fig3.add_subplot()
plot.plot(len_arr, res3[0], label="Гномья сортировка")
plot.plot(len_arr, res3[2], label="Поразрядная сортировка")
plot.plot(len_arr, res3[1], label="Сортировка выбором")
plt.legend()
plt.grid()
plt.title("Временные характеристики алгоритмов сортировки (произвольный случай)")
plt.ylabel("Затраченное время (мкс)")
plt.xlabel("Длина массива")
print("Слйчайный порядок (с.с.): ", res3)

plt.show()
