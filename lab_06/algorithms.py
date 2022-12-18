from random import random, shuffle

INF = 1e10
EPS = 1e-5

ALPHA = 0.5
PHO = 0.5
TMAX = 100

DEBUG = False
ant_to_debug_n = [2, ]
t_to_debug = [0, 50, 99]


def print_matrix(D, n_cities, message='Матрица:'):
    print(message)
    for i in range(n_cities):
        for j in range(n_cities):
            if D[i][j] != INF:
                print("%3d" % D[i][j], end=' ')
            else:
                print("INF", end=' ')
        print()


def count_way_lenth(D, vis_cities):
    length = 0

    for l in range(1, len(vis_cities)):
        i = vis_cities[l - 1]
        j = vis_cities[l]
        length += D[i][j]

    return length


def ant_search(D, n_cities, alpha=ALPHA, pho=PHO, tmax=TMAX):
    print('Муравьиный алгоритм')
    Q = 0
    for i in range(n_cities):
        for j in range(i):
            if D[i][j] < INF:
                Q += D[i][j]
    beta = 1 - alpha

    # Инициализация ребер — присвоение видимости eta
    # и начальной концентрации феромона.
    eta = [[0 for i in range(n_cities)] for j in range(n_cities)]
    tau = [[0 for i in range(n_cities)] for j in range(n_cities)]
    for i in range(n_cities):
        for j in range(i):
            eta[i][j] = 1 / D[i][j]
            eta[j][i] = 1 / D[j][i]
            tau[i][j] = 2 * EPS
            tau[j][i] = 2 * EPS

    min_way_length = INF

    # Цикл по времени жизни колонии
    for t in range(tmax):
        vis_cities = [[i] for i in range(n_cities)]

        #  Цикл по всем муравьям
        for k in range(n_cities):
            # Построить маршрут
            while len(vis_cities[k]) != n_cities:

                if DEBUG and k in ant_to_debug_n and t in t_to_debug:
                    print(f'\n\nОтладочный муравей {k} на {t}-й итерации')
                    print(
                        f'    Поиск {len(vis_cities[k]) + 1}-го города для посещения после посещения городов {vis_cities[k]}')

                P_ch = [0 for i in range(n_cities)]
                for j in range(n_cities):
                    if j not in vis_cities[k]:
                        i = vis_cities[k][-1]
                        P_ch[j] = (tau[i][j] ** alpha) * (eta[i][j] ** beta)

                P_zn = sum(P_ch)
                for j in range(n_cities):
                    P_ch[j] /= P_zn

                # Следующий город
                #  0         pk[0]  pk[1]    pk[2]       pk[2]  1
                #  |----------|------|--------|---x--------|----|
                probability = random()
                summ, j = 0, 0
                while summ < probability:
                    summ += P_ch[j]
                    j += 1
                vis_cities[k].append(j - 1)
                if DEBUG and k in ant_to_debug_n and t in t_to_debug:

                    print(f'        Подсчитанные вероятности посещения городов: {P_ch}')
                    print(f'        Результат генерации случ. значение от 0 до 1: {probability}')
                    print(f'        Выбранный город": {j - 1}')
                    print(f'        Полученный список посещенных городов": {vis_cities[k]}')

            #vis_cities[k].append(vis_cities[k][0])
            way_length = count_way_lenth(D, vis_cities[k])

            if DEBUG and k in ant_to_debug_n and t in t_to_debug:
                print(f'Итоговый результат отладочного муравья:\n'
                      f'    список посещенных городов: {vis_cities[k]}; длина пути: {way_length}')

            # Выбрать лучшее решение
            if way_length < min_way_length:
                min_way_length = way_length
                min_way = vis_cities[k]

        # Обновление следов феромона на ребрах
        for i in range(n_cities):
            for j in range(i):
                delta_tau = 0
                # подсчет добавления
                for k in range(n_cities):
                    way_length = count_way_lenth(D, vis_cities[k])
                    for m in range(1, len(vis_cities[k])):
                        if (vis_cities[k][m], vis_cities[k][m - 1]) in ((i, j), (j, i)):
                            delta_tau += Q / way_length
                            break

                # испарение и добавление
                tau[i][j] = tau[i][j] * (1 - pho) + delta_tau
                if tau[i][j] < EPS:  # проверка, чтобы феромон не обнулился
                    tau[i][j] = EPS
                tau[j][i] = tau[i][j]
        if DEBUG and t in t_to_debug:
            print(f'\n\nПосле {t}-й отладочной итерации')
            print_matrix(tau, n_cities, message=f'    Матрица следов феромонов:')
            print(f'Наиболее оптимальный путь: {min_way} длиной {min_way_length}')

    return min_way_length, min_way


# генератор перестановок
def next_set(a, n):
    # инициализация
    if not a:
        for i in range(n):
            a.append(i)
        return True

    # просмотреть текущую перестановку справа налево и при этом следить за тем,
    # чтобы каждый следующий элемент перестановки был не более чем предыдущий.
    j = n - 2
    while j != -1 and a[j] > a[j + 1]:
        j -= 1
    if j == -1:
        return False  # больше перестановок нет

    # cнова просмотреть пройденный путь справа налево пока не дойдем до первого числа,
    # которое больше чем отмеченное на предыдущем шаге.
    k = n - 1
    while a[j] > a[k]:
        k -= 1
    # поменять местами два полученных элемента.
    a[j], a[k] = a[k], a[j]

    # сортируем оставшуюся часть последовательности
    l = j + 1
    r = n - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return True


def full_search(D, n_cities):
    min_way_length = INF
    min_way = None
    cur_way = []

    while next_set(cur_way, n_cities):
        cur_way_lenth = count_way_lenth(D, cur_way)
        if cur_way_lenth < min_way_length:
            min_way_length = cur_way_lenth
            min_way = cur_way

    return min_way_length, min_way