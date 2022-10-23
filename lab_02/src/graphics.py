# Артюхин Николай ИУ7-51Б ЛР2 (Алгоритмы умножения матриц) - модуль замеров процессорного времени + графики

import time
import random
import matplotlib.pyplot as plt
from mult_matrix_algs import *

N = 1 # количество итераций для замеров времени


def generate_matrix(n):
    matr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matr[i][j] = random.randint(0, 100)
    return matr


def proc_time(m1, m2, iters, func):
    t1 = time.process_time()
    for i in range(iters):
        func(m1, m2)
    t2 = time.process_time()
    return (t2 - t1) / iters


def time_measure():
    res_stand = []
    res_vin = []
    res_vin_opt = []

    ns = [i for i in range(100, 501, 100)]

    for n in ns:
        a = generate_matrix(n)
        b = generate_matrix(n)
        res_stand.append(proc_time(a, b, N, standart_mult_matr))
        res_vin.append(proc_time(a, b, N, vinograd_mult_matr))
        res_vin_opt.append(proc_time(a, b, N, vinograd_optimized_mult_matr))
        print(n)

    res_stand1 = []
    res_vin1 = []
    res_vin_opt1 = []

    for n in ns:
        a = generate_matrix(n + 1)
        b = generate_matrix(n + 1)
        res_stand1.append(proc_time(a, b, N, standart_mult_matr))
        res_vin1.append(proc_time(a, b, N, vinograd_mult_matr))
        res_vin_opt1.append(proc_time(a, b, N, vinograd_optimized_mult_matr))
        print(n)

    len_arr = [100, 200, 300, 400, 500]  # длины матриц

    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(len_arr, res_stand, label="Стандартный алгоритм")
    plot.plot(len_arr, res_vin, label="Алгоритм Винограда")
    plot.plot(len_arr, res_vin_opt, label="Алгоритм Винограда (оптим.)")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов умножения матриц (n * n)")
    plt.ylabel("Затраченное время (c)")
    plt.xlabel("Размер матриц (n)")

    fig2 = plt.figure(figsize=(10, 7))
    plot = fig2.add_subplot()
    plot.plot(len_arr, res_stand1, label="Стандартный алгоритм")
    plot.plot(len_arr, res_vin1, label="Алгоритм Винограда")
    plot.plot(len_arr, res_vin_opt1, label="Алгоритм Винограда (оптим.)")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов умножения матриц (n + 1 * n + 1)")
    plt.ylabel("Затраченное время (c)")
    plt.xlabel("Размер матриц (n)")

    plt.show()

    print("matrix size - n * n")
    print("res_standart:", res_stand)
    print()
    print("res_vinograd:", res_vin)
    print()
    print("res_vinograd_optimized:", res_vin_opt)

    print("matrix size - (n + 1) * (n + 1)")
    print("res_standart:", res_stand1)
    print()
    print("res_vinograd:", res_vin1)
    print()
    print("res_vinograd_optimezed:", res_vin_opt1)


if __name__ == "__main__":
    time_measure()