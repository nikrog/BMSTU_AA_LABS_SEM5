from dist_algorythms import *
import string
import random
import time

import matplotlib.pyplot as plt

N = 100000
y_time_lev_iter = []
y_time_dam_lev_iter = []
y_time_dam_lev_rec = []
y_time_dam_lev_rec_cach = []

len_arr = []


def test(len):
    time_lev_iter = 0
    time_dam_lev_iter = 0
    time_dam_lev_rec = 0
    time_dam_lev_rec_cach = 0


    for i in range(N):
        s1 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))
        s2 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))

        start = time.process_time()
        lowenstein_dist_non_recursive(s1, s2, False)
        stop = time.process_time()

        time_lev_iter += stop - start

        start = time.process_time()
        damerau_lowenstein_dist_non_recursive(s1, s2, False)
        stop = time.process_time()

        time_dam_lev_iter += stop - start

        if i < 10:
            start = time.process_time()
            damerau_lowenstein_dist_recursive(s1, s2)
            stop = time.process_time()

            time_dam_lev_rec += stop - start
        if i < N / 100:
            start = time.process_time()
            damerau_lowenstein_dist_recursive_cache(s1, s2, False)
            stop = time.process_time()

            time_dam_lev_rec_cach += stop - start

    len_arr.append(len)
    y_time_lev_iter.append((time_lev_iter / N) * 1000000)
    y_time_dam_lev_iter.append((time_dam_lev_iter / N) * 1000000)
    y_time_dam_lev_rec.append((time_dam_lev_rec / 100) * 1000000)
    y_time_dam_lev_rec_cach.append((time_dam_lev_rec_cach / (N/100)) * 1000000)


    return (time_lev_iter / N) * 1000000, (time_dam_lev_iter / N) * 1000000, \
           (time_dam_lev_rec / 10) * 1000000, (time_dam_lev_rec_cach / (N/100)) * 1000000


def print_results(count):
    time_lev_iter, time_dam_lev_iter, time_dam_lev_rec, time_dam_lev_rec_cach = test(count)
    print("\n--------------------------------------------------------------------------------------")
    print("Время работы функции при n = ", count)
    print("Нерекурсивный алгоритм поиска расстояния Левенштейна: ", "{0:.6f}".format(time_lev_iter), "мкс")
    print("Нерекурсивный алгоритм поиска расстояния Дамерау-Левенштейна: ", "{0:.6f}".format(time_dam_lev_iter), "мкс")
    print("Рекурсивный алгоритм (без кеша) поиска расстояния Дамерау-Левенштейна: ", "{0:.6f}".format(time_dam_lev_rec), "мкс")
    print("Рекурсивный алгоритм (с кешем - матрица) поиска расстояния Дамерау-Левенштейна: ", "{0:.6f}".format(time_dam_lev_rec_cach), "мкс")

    return

if __name__ == "__main__":
    for i in range(10):
       print_results(i)

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(len_arr, y_time_lev_iter, label="Расст. Левенштейна(нерек)")
    plot.plot(len_arr, y_time_dam_lev_iter, label="Расст. Дамерау-Левенштейна(нерек)")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов вычисления расстояния")
    plt.ylabel("Затраченное время (мкс)")
    plt.xlabel("Длина слов (символы)")


    fig1 = plt.figure(figsize = (10, 7))
    plot = fig1.add_subplot()
    plot.plot(len_arr, y_time_dam_lev_rec, label="Расст. Дамерау-Левенштейна(рек)")
    plot.plot(len_arr, y_time_dam_lev_rec_cach, label="Расст. Дамерау-Левенштейна(рек, кеш)")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов вычисления расстояния")
    plt.ylabel("Затраченное время (мкс)")
    plt.xlabel("Длина слов (символы)")

    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    #plot.plot(len_arr, y_time_lev_iter, label="Расст. Левенштейна(нерек)")
    plot.plot(len_arr, y_time_dam_lev_iter, label="Расст. Дамерау-Левенштейна(нерек)")
    plot.plot(len_arr, y_time_dam_lev_rec, label="Расст. Дамерау-Левенштейна(рек)")
    plot.plot(len_arr, y_time_dam_lev_rec_cach, label="Расст. Дамерау-Левенштейна(рек, кеш)")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов вычисления расстояния")
    plt.ylabel("Затраченное время (мкс)")
    plt.xlabel("Длина слов (символы)")

    plt.show()