from algorithms import *


def print_matrix(D, n_cities, message='Матрица смежности:'):
    print(message)
    for i in range(n_cities):
        for j in range(n_cities):
            if D[i][j] != INF:
                print("%3d" % D[i][j], end=' ')
            else:
                print("INF", end=' ')
        print()

def test(D, n_cities):
        print_matrix(D, n_cities)

        print('\n')
        answ_full, way_full = full_search(D, n_cities)
        print(f'Результат алгоритма полного перебора:\n '
              f'{answ_full}, {way_full}')
        print('\n')

        answ_ant, way_ant = ant_search(D, n_cities)
        print(f'Результат муравьиного алгоритма:\n '
              f'{answ_ant}, {way_ant}')
        print('\n')
        print("Ошибка: ", answ_ant - answ_full)

def tests_alg():
    D1 = [[0, 3, 4, 7],
          [3, 0, 3, 7],
          [4, 3, 0, 7],
          [7, 7, 7, 0]]

    n_cities1 = len(D1)

    D2 = [[0, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1],
          [1, 1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1, 0]]

    n_cities2 = len(D2)

    D3 = [[0, 9771, 8531, 2010, 1983, 7296, 7289, 3024, 1011],
          [9771, 0, 7531, 4865, 5494, 6812, 4755, 7780, 7641],
          [8531, 7531, 0, 1819, 9297, 7506, 5781, 5804, 7334],
          [2010, 4865, 1819, 0, 3662, 9597, 2876, 8188, 9227],
          [1983, 5494, 9297, 3662, 0, 8700, 4754, 7445, 3834],
          [7296, 6812, 7506, 9597, 8700, 0, 4216, 5553, 8215],
          [7289, 4755, 5781, 2876, 4754, 4216, 0, 4001, 4715],
          [3024, 7780, 5804, 8188, 7445, 5553, 4001, 0, 9522],
          [1011, 7641, 7334, 9227, 3834, 8215, 4715, 9522, 0]]

    n_cities3 = len(D3)

    test(D1, n_cities1)
    test(D2, n_cities2)
    test(D3, n_cities3)

if __name__ == '__main__':
    tests_alg()