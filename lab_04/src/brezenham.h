#ifndef BREZENHAM_H
#define BREZENHAM_H

#include <ui_mainwindow.h>
#include <math.h>

#include <thread>
#include <mutex>
#include <vector>
#include <chrono>
#include <ctime>
#include <time.h>
#include <iostream>


#define WIN_X 709
#define WIN_Y 709
#define PI 3.1415
#define PT_SIZE 0.1

#define MAX_THREADS 64

#define MAX_DIAM 10000
#define MIN_DIAM 500
#define DIAM_STEP 500

#define ITERATIONS 500

struct request
{
    int algorithm;
    QColor color;
    QGraphicsScene *scene;

    bool is_draw;
};

struct spektr_params
{
    int d;
    int threads_count;
};

struct point
{
    double x;
    double y;
};


enum types
{
    PARALLEL,
    NO_PARALLEL
};

using point_t = struct point;

using request_t = struct request;

using spektr_t = struct spektr_params;

int sign(const int &number);
void swap(int &dx, int &dy);

void calculate_beam_no_parallel(const request_t &request, const spektr_t &params);
void calculate_beam_parallel(const request_t &request, const spektr_t &params);

void calculate_line(const request_t &request, const point_t &pt1, const point_t &pt2);

void breshenham_float(const request_t &request, const point_t &pt1, const point_t &pt2);

double time_mes_no_parallel(const request_t &request, const spektr_t &params);
double time_mes_parallel(const request_t &request, const spektr_t &params);

#endif // BREZENHAM_H
