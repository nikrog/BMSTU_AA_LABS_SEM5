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
    Q = 0
    for i in range(n_cities):
        for j in range(i):
            if D[i][j] < INF:
                Q += D[i][j]
    beta = 1 - alpha

    eta = [[0 for i in range(n_cities)] for j in range(n_cities)]
    tau = [[0 for i in range(n_cities)] for j in range(n_cities)]
    for i in range(n_cities):
        for j in range(i):
            eta[i][j] = 1 / D[i][j]
            eta[j][i] = 1 / D[j][i]
            tau[i][j] = 2 * EPS
            tau[j][i] = 2 * EPS

    min_way_length = INF

    for t in range(tmax):
        vis_cities = [[i] for i in range(n_cities)]

        for k in range(n_cities):
            while len(vis_cities[k]) != n_cities:

                P_ch = [0 for i in range(n_cities)]
                for j in range(n_cities):
                    if j not in vis_cities[k]:
                        i = vis_cities[k][-1]
                        P_ch[j] = (tau[i][j] ** alpha) * (eta[i][j] ** beta)

                P_zn = sum(P_ch)
                for j in range(n_cities):
                    P_ch[j] /= P_zn

                probability = random()
                summ, j = 0, 0
                while summ < probability:
                    summ += P_ch[j]
                    j += 1
                vis_cities[k].append(j - 1)

            way_length = count_way_lenth(D, vis_cities[k])

            if way_length < min_way_length:
                min_way_length = way_length
                min_way = vis_cities[k]

        for i in range(n_cities):
            for j in range(i):
                delta_tau = 0

                for k in range(n_cities):
                    way_length = count_way_lenth(D, vis_cities[k])
                    for m in range(1, len(vis_cities[k])):
                        if (vis_cities[k][m], vis_cities[k][m - 1]) in ((i, j), (j, i)):
                            delta_tau += Q / way_length
                            break


                tau[i][j] = tau[i][j] * (1 - pho) + delta_tau
                if tau[i][j] < EPS:
                    tau[i][j] = EPS
                tau[j][i] = tau[i][j]

    return min_way_length, min_way


def next_way(a, n):
    if not a:
        for i in range(n):
            a.append(i)
        return True

    j = n - 2
    while j != -1 and a[j] > a[j + 1]:
        j -= 1
    if j == -1:
        return False

    k = n - 1
    while a[j] > a[k]:
        k -= 1
    a[j], a[k] = a[k], a[j]

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

    while next_way(cur_way, n_cities):
        cur_way_lenth = count_way_lenth(D, cur_way)
        if cur_way_lenth < min_way_length:
            min_way_length = cur_way_lenth
            min_way = cur_way

    return min_way_length, min_way