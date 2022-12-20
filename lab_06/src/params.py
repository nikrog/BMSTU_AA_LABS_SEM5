from algorithms import *
#from time_cmp import generate_matrix_random, generate_matrix_one_way, diff
from random import randint, choices
from tests import print_matrix
from copy import copy
import pandas as pd

alphas = [0.1, 0.25, 0.5, 0.75, 0.9]
#alphas = [0.1]
pos = copy(alphas)
#tmaxs = [100, 200, 300, 400, 500]
tmaxs = [20, 50, 100, 200, 500]


small_diff = 10
big_diff = 1000
local_diff = 1
# diff = 30
n_cities = 9
file_i = 9

path = 'D:/AnalysisAlgorithms/lab_06/table'
#df_file = path + 'df3.xlsx'



def generate_matrix_one_way(n):
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
            if i == j + 1:
                D[i][j] = small_diff - local_diff
                D[j][i] = small_diff - local_diff
            elif (i + j) % 4 == 0:
                D[i][j] = small_diff + local_diff
                D[j][i] = small_diff + local_diff
            else:
                D[i][j] = small_diff
                D[j][i] = small_diff
    D[0][n - 1] = small_diff - local_diff
    D[n - 1][0] = small_diff - local_diff
    return D


def generate_matrix_random(n):
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
                rand_num = randint(1, 2)
                # res = choices([rand_num, INF], weights=[0.8, 0.2])[0]
                res = rand_num
                D[i][j] = res
                D[j][i] = res
    return D

def generate_matrix_all_same(n):
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
                rand_num = randint(1, big_diff)
                # res = choices([rand_num, INF], weights=[0.8, 0.2])[0]
                res = rand_num
                D[i][j] = res
                D[j][i] = res
    return D


def make_table():
    df = pd.DataFrame(columns=['alpha', 'po', 'tmax', 'g1_small_matr', 'g2_big_matr_small_diff',
                               'g3_big_matr_big_diff', 'mediana'])

    D_rand = generate_matrix_random(n_cities)
    print_matrix(D_rand, n_cities-4, message='D_small_matr')

    D_one_way = generate_matrix_one_way(n_cities)
    print_matrix(D_one_way, n_cities, message='D_big_matr_small_diff')

    D_all_same = generate_matrix_all_same(n_cities)
    print_matrix(D_all_same, n_cities, message='D_big_matr_big_diff')

    answer_full_rand, _ = full_search(D_rand, n_cities)
    answer_full_one_way, _ = full_search(D_one_way, n_cities)
    answer_full_all_same, _ = full_search(D_all_same, n_cities)

    for alpha in alphas:
        for po in pos:
            for tmax in tmaxs:
                answer_ant_rand, _ = ant_search(D_rand, n_cities, alpha, po, tmax)
                answer_ant_one_way, _ = ant_search(D_one_way, n_cities, alpha, po, tmax)
                answer_ant_all_same, _ = ant_search(D_all_same, n_cities, alpha, po, tmax)
                med_arr = []
                med_arr.append(answer_ant_rand - answer_full_rand)
                med_arr.append(answer_ant_one_way - answer_full_one_way)
                med_arr.append(answer_ant_all_same - answer_full_all_same)
                med_arr.sort()
                results = {'alpha': alpha, 'po': po, 'tmax': tmax,
                           'g1_small_matr': answer_ant_rand - answer_full_rand,
                           'g2_big_matr_small_diff': answer_ant_one_way - answer_full_one_way,
                           'g3_big_matr_big_diff': answer_ant_all_same - answer_full_all_same,
                           'mediana': (med_arr[1])}
                df = df.append(results, ignore_index=True)
                print(results)

    return df


if __name__ == '__main__':
    print()
    df = make_table()
    #df.show()