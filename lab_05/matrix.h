//
// Created by arper on 04.12.2022.
//

#ifndef LAB_05_MATRIX_H
#define LAB_05_MATRIX_H

#include <random>
#include <vector>
#include <iostream>
#include <queue>
#include <thread>
#include <math.h>
#include <string>


struct matrix_s
{
    std::vector<std::vector<double>> data;
    size_t size;
    double det; // определитель матрицы
    double avg;
    double max;
};

using matrix_t = struct matrix_s;

matrix_t generate_matrix(size_t size);
matrix_t copy_matrix(matrix_t matrix);
void print_matrix(matrix_t matrix);
void mult_matrix(matrix_t &matrix);
void triangulate_matr(matrix_t &matrix);
void get_avg(matrix_t &matrix);
void get_max(matrix_t &matrix);
void get_determinate(matrix_t &matrix);
void fill_matrix(matrix_t &matrix);

#endif //LAB_05_MATRIX_H
