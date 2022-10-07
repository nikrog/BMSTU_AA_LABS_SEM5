# Артюхин Николай ИУ7-51Б ЛР3
# Модуль автоматического тестирования функций сортирвки

from sorting_algorithms import *


class TestSorts:
    def __init__(self, function, func_name):
        self.function = function
        self.func_name = func_name

    def test_sorted_array(self):
        print(f'Testing sorted array for {self.func_name}')
        arr = [0]
        assert self.function(arr) == arr
        arr = [5, 5, 5, 5]
        assert self.function(arr) == arr
        arr = [3, 10, 250, 2080]
        assert self.function(arr) == arr
        arr = [-108, -10, 10, 108]
        assert self.function(arr) == arr
        print('OK\n')

    def test_reverse_sorted_array(self):
        print(f'Testing reverse sorted array for {self.func_name}')
        arr = [78, 44, 32, 1]
        assert self.function(arr) == [1, 32, 44, 78]
        arr = [108, 10, -10, -108]
        assert self.function(arr) == [-108, -10, 10, 108]
        arr = [12100, 108, 10, -10, -108]
        assert self.function(arr) == [-108, -10, 10, 108, 12100]
        print('OK\n')

    def test_random_array(self):
        print(f'Testing random array for {self.func_name}')
        arr = [234, 7, -11, 68, -3, 1005]
        assert self.function(arr) == [-11, -3, 7, 68, 234, 1005]
        arr = [-90, -356, -4, -1058]
        assert self.function(arr) == [-1058, -356, -90, -4]
        arr = [-90, 68, -356, -4, -1058, -90, 68]
        assert self.function(arr) == [-1058, -356, -90, -90, -4, 68, 68]
        print('OK\n')

    def run_tests(self):
        self.test_sorted_array()
        self.test_reverse_sorted_array()
        self.test_random_array()


if __name__ == '__main__':
    test = TestSorts(gnome_sort, 'gnome_sort')
    test.run_tests()
    test = TestSorts(radix_sort, 'radix_sort')
    test.run_tests()
    test = TestSorts(selection_sort, 'selection_sort')
    test.run_tests()
