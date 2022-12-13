#include <iostream>

#include "conveyor.h"

void menu()
{
    printf("\n\n Трехэтапная обработка матрицы \
        \n\tДействия: \
        \n\t1. Последовательная обработка \
        \n\t2. Конвейерная обработка \
        \n\t3. Замерить время \
        \n\t4. Вывести информацию об этапах обработки \
      \n\t0. Выход\n\n");
}


int main(void)
{
    int act = -1;

    while (act != 0)
    {
        menu();

        std::cout << "Действие >> ";
        std::cin >> act;

        if (act == 1)
        {
            int size = 0, count = 0;

            std::cout << "\n\nРазмер квадратной матрицы >> ";
            std::cin >> size;

            std::cout << "Количество матриц >> ";
            std::cin >> count;

            parse_linear(count, size, true);
        }
        else if (act == 2)
        {
            int size = 0, count = 0;

            std::cout << "\n\nРазмер квадратной матрицы >> ";
            std::cin >> size;

            std::cout << "Количество матриц >> ";
            std::cin >> count;

            parse_parallel(count, size, true);
        }
        else if (act == 3)
        {
            time_mes();
        }
        else if (act == 4)
        {
            info_stages();
        }
        else if (act == 0)
        {
            printf("\nУспешный выход!\n");
        }
        else
        {
            printf("\nОшибка: Несуществующий номер действия! (должен быть от 0 до 4)\n");
        }
    }
    return 0;
}
