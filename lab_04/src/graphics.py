import matplotlib.pyplot as plt


def graph_different_threads():
    threads = [1, 2, 4, 8, 16, 32, 64]
    time_threads = [0.000794, 0.000457, 0.000403, 0.000511, 0.000976, 0.002083, 0.003656]
    time_noparallel = [0.000630145]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(threads, time_threads, label="Многопоточность")
    plot.plot(threads, time_noparallel * 7, label="Без распараллеливания")

    plt.legend()
    plt.grid()
    plt.title("Cравнение времени работы последовательной и многопоточной реализаций")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Количество потоков")

    plt.show()


def graph_different_diams():
    diams = [i for i in range(500, 10001, 500)]
    time_4threads = [0.000385, 0.000544, 0.000719, 0.000876, 0.001053, 0.001216, 0.001371, 0.001524, 0.001692,
                     0.001854, 0.002019, 0.002167, 0.002292, 0.002412, 0.002503, 0.002691, 0.002881, 0.003144,
                     0.003322, 0.003465]
    time_noparallel = [0.000640, 0.001202, 0.001761, 0.002332, 0.002888, 0.003467, 0.003996, 0.004576, 0.005130,
                       0.005697, 0.006247, 0.006801, 0.007350, 0.007922, 0.008476, 0.009031, 0.009596, 0.010260,
                       0.010735, 0.011408]
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(diams, time_4threads, label="Распараллеивание на 4 потока")
    plot.plot(diams, time_noparallel, label="Без распараллеливания")

    plt.legend()
    plt.grid()
    plt.title("Сравнение времени работы реализаций алгоритмов на разных длинах отрезков в спектре")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина отрезка в спектре")

    plt.show()


if __name__ == "__main__":
    graph_different_threads()
    graph_different_diams()
