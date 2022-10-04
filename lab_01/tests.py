# Артюхин Николай ИУ7-51Б ЛР1

from dist_algorythms import *

def random_string(lenght):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(lenght))

class TestDistance:
    def __init__(self, function, func_name, exchange):
        self.function = function
        self.func_name = func_name
        self.exchange = exchange

    def test_empty_str(self):
        print(f'Testing empty string(s) for {self.func_name}')
        assert self.function("", "") == 0
        assert self.function("", "abc") == 3
        assert self.function("abc", "") == 3
        print('OK\n')

    def test_equal_str(self):
        print(f'Testing equal strings for {self.func_name}')
        assert self.function("art", "art") == 0
        assert self.function("a", "a") == 0
        print('OK\n')

    def test_different_str(self):
        print(f'Testing different strings for {self.func_name}')
        assert self.function("кот", "скат") == 2
        assert self.function("гора", "горы") == 1
        assert self.function("солнце", "солнцестояние") == 7
        assert self.function("солнцестояние", "солнце") == 7
        assert self.function("аргон", "арнон") == 1
        assert self.function("a", "e") == 1
        assert self.function("af", "f") == 1
        assert self.function("a", "af") == 1
        assert self.function("de", "ge") == 1
        assert self.function("hf", "nj") == 2
        assert self.function("abc", "cd") == 3
        print('OK\n')

    def test_exchange_symbols(self):
        print(f'Testing exchange for {self.func_name}')
        if not self.exchange:
            assert self.function("ab", "ba") == 2
            assert self.function("институт", "ниститту") == 4
            assert self.function("class", "clsas") == 2
            assert self.function("12345", "12435") == 2
        else:
            assert self.function("ab", "ba") == 1
            assert self.function("институт", "ниститту") == 2
            assert self.function("class", "clsas") == 1
            assert self.function("12345", "12435") == 1

        print('OK\n')

    def run_tests(self):
        self.test_empty_str()
        self.test_equal_str()
        self.test_different_str()
        self.test_exchange_symbols()


if __name__ == '__main__':
    test = TestDistance(lowenstein_dist_non_recursive, 'lowenstein_dist_non_recursive', False)
    test.run_tests()
    test = TestDistance(damerau_lowenstein_dist_non_recursive, 'damerau_lowenstein_dist_non_recursive', True)
    test.run_tests()
    test = TestDistance(damerau_lowenstein_dist_recursive, 'damerau_lowenstein_dist_recursive', True)
    test.run_tests()
    test = TestDistance(damerau_lowenstein_dist_recursive_cache, 'damerau_lowenstein_dist_recursive_cache', True)
    test.run_tests()
