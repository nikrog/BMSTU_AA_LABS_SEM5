import matplotlib.pyplot as plt


def graph_different_threads():
    threads = [1, 2, 4, 8, 16, 32]
    time_threads = [0.000794, 0.000457, 0.000403, 0.000511, 0.000976, 0.002083]
    time_noparallel = [0.000730145]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(threads, time_threads, label="Многопоточность")
    plot.plot(threads, time_noparallel * 6, label="Без распараллеливания")

    plt.legend()
    plt.grid()
    plt.title("Cравнение времени работы последовательной и многопоточной реализаций")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Количество потоков")

    plt.show()


def graph_different_sizes():
    size = [i for i in range(10, 51, 5)]
    time_lin = [0.1489, 0.2205, 0.2945, 0.3676, 0.4384, 0.5104, 0.5825, 0.6599, 0.7327]
    time_conv = [0.0852, 0.1161, 0.1526, 0.2007, 0.2288, 0.2724, 0.2990, 0.3355, 0.3948]
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(size, time_lin, label="Последовательная обработка")
    plot.plot(size, time_conv, label="Конвейерная обработка")

    plt.legend()
    plt.grid()
    plt.title("Сравнение времени работы реализаций последовательного и конвейрного алгоритмов обработки матриц")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Линейный размер квадратных матриц")

    plt.show()


if __name__ == "__main__":
    graph_different_sizes()
