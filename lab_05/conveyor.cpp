#include "conveyor.h"

double time_now = 0;

std::vector<double> t1;
std::vector<double> t2;
std::vector<double> t3;
std::vector<double> min;
std::vector<double> max;
std::vector<double> avg;
std::vector<double> mid;
std::vector<double> time1;
std::vector<double> time2;
std::vector<double> time3;
std::vector<double> sum;
std::vector<double> sumsys;

void log_linear(matrix_t &matrix, int task_num, int stage_num, void (*func)(matrix_t &), bool is_print)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double start_res_time = time_now, res_time = 0;

    time_start = std::chrono::system_clock::now();
    func(matrix);
    time_end = std::chrono::system_clock::now();

    res_time = (std::chrono::duration_cast<std::chrono::nanoseconds>
            (time_end - time_start).count()) / 1e9;


    time_now = start_res_time + res_time;

    if (is_print)
        printf("Task: %3d, Stage: %3d, Start at %.6f, End at %.6f\n",
               task_num, stage_num, start_res_time, start_res_time + res_time);

}



void log_conveyor(matrix_t &matrix, int task_num, int stage_num, void (*func)(matrix_t &), bool is_print)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double res_time = 0;

    time_start = std::chrono::system_clock::now();
    func(matrix);
    time_end = std::chrono::system_clock::now();

    res_time = (std::chrono::duration_cast<std::chrono::nanoseconds>
            (time_end - time_start).count()) / 1e9;

    double start_res_time;

    if (stage_num == 1)
    {
        start_res_time = t1[task_num - 1];

        t1[task_num] = start_res_time + res_time;
        t2[task_num - 1] = t1[task_num];
        //time1[task_num - 1] = res_time;
        time1[task_num] = res_time;
    }
    else if (stage_num == 2)
    {
        start_res_time = t2[task_num - 1];

        t2[task_num] = start_res_time + res_time;
        t3[task_num - 1] = t2[task_num];
        //time2[task_num - 1] = res_time;
        time2[task_num - 1] = start_res_time - t1[task_num - 1];
    }
    else if (stage_num == 3)
    {
        start_res_time = t3[task_num - 1];
        //time3[task_num - 1] = res_time;
        time3[task_num - 1] = start_res_time - t2[task_num - 1];
    }

    if (is_print)
        printf("Task: %3d, Stage: %3d, Start at %.6f, End at %.6f\n",
               task_num, stage_num, start_res_time, start_res_time + res_time);

}


void stage1_linear(matrix_t &matrix, int task_num, bool is_print)
{
    log_linear(matrix, task_num, 1, mult_matrix, is_print);
}

void stage2_linear(matrix_t &matrix, int task_num, bool is_print)
{
    log_linear(matrix, task_num, 2,triangulate_matr, is_print);
}


void stage3_linear(matrix_t &matrix, int task_num, bool is_print)
{
    log_linear(matrix, task_num, 3, get_determinate, is_print);
}


void parse_linear(int count, size_t size, bool is_print)
{

    time_now = 0;

    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    queues_t queues = {.q1 = q1, .q2 = q2, .q3 = q3};

    for (int i = 0; i < count; i++)
    {
        matrix_t res = generate_matrix(size);

        queues.q1.push(res);
    }

    for (int i = 0; i < count; i++)
    {
        matrix_t matrix = queues.q1.front();
        stage1_linear(matrix, i + 1, is_print);
        queues.q1.pop();
        queues.q2.push(matrix);

        matrix = queues.q2.front();
        stage2_linear(matrix, i + 1, is_print); // Stage 2
        queues.q2.pop();
        queues.q3.push(matrix);

        matrix = queues.q3.front();
        stage3_linear(matrix, i + 1, is_print); // Stage 3
        queues.q3.pop();

        /*if (is_print)
           print_matrix(matrix);*/
    }
}



void stage1_parallel(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2, std::queue<matrix_t> &q3, bool is_print)
{
    int task_num = 1;

    std::mutex m;

    while(!q1.empty())
    {
        m.lock();
        matrix_t matrix = q1.front();
        m.unlock();

        log_conveyor(matrix, task_num++, 1, mult_matrix, is_print);
        m.lock();
        q2.push(matrix);
        q1.pop();
        m.unlock();
    }
}


void stage2_parallel(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2, std::queue<matrix_t> &q3, bool is_print)
{
    int task_num = 1;

    std::mutex m;

    do
    {
        m.lock();
        bool is_q2empty = q2.empty();
        m.unlock();

        if (!is_q2empty)
        {
            m.lock();
            matrix_t matrix = q2.front();
            m.unlock();

            log_conveyor(matrix, task_num++, 2, triangulate_matr, is_print);
            m.lock();
            q3.push(matrix);
            q2.pop();
            m.unlock();
        }
    } while (!q1.empty() || !q2.empty());
}


void stage3_parallel(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2, std::queue<matrix_t> &q3, bool is_print)
{
    int task_num = 1;

    std::mutex m;

    do
    {
        m.lock();
        bool is_q3empty = q3.empty();
        m.unlock();

        if (!is_q3empty)
        {
            m.lock();
            matrix_t matrix = q3.front();
            m.unlock();

            log_conveyor(matrix, task_num++, 3, get_determinate, is_print);
            m.lock();
            q3.pop();
            m.unlock();
        }
    } while (!q1.empty() || !q2.empty() || !q3.empty());
}

void sort_arr(std::vector<double> &arr, int size)
{
    double t;
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                t = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = t;
            }
        }
    }
}

double get_max_(std::vector<double> &arr, int size)
{
    double max = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

double get_min_(std::vector<double> &arr, int size)
{
    double min = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}

double get_avg_(std::vector<double> &arr, int size)
{
    double sum = 0, avg;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    avg = sum / size;
    return avg;
}

double get_mid_(std::vector<double> &arr, int size)
{
    double mid;
    sort_arr(arr, size);
    int ind = size / 2;
    if (size % 2 == 0)
    {
        mid = (arr[ind] + arr[ind - 1]) / 2;
    }
    else
    {
        mid = arr[ind];
    }
    return mid;
}


void parse_parallel(int count, size_t size, bool is_print)
{
    t1.resize(count + 1);
    t2.resize(count + 1);
    t3.resize(count + 1);
    time1.resize(count + 1);
    time2.resize(count + 1);
    time3.resize(count + 1);
    min.resize(3);
    max.resize(3);
    avg.resize(3);
    mid.resize(3);
    sum.resize(count + 1);
    sumsys.resize(count + 1);
    double minq = 0, maxq = 0, avgq, midq, mins, maxs, avgs, mids;

    for (int i = 0; i < count + 1; i++)
    {
        t1[i] = 0;
        t2[i] = 0;
        t3[i] = 0;
        time1[i] = 0;
        time2[i] = 0;
        time3[i] = 0;
        sum[i] = 0;
        sumsys[i] = 0;
    }
    for(int i = 0; i < 3; i++)
    {
        min[i] = 0;
        max[i] = 0;
        avg[i] = 0;
        mid[i] = 0;
    }

    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    queues_t queues = {.q1 = q1, .q2 = q2, .q3 = q3};


    for (int i = 0; i < count; i++)
    {
        matrix_t res = generate_matrix(size);

        q1.push(res);
    }

    std::thread threads[THREADS];

    threads[0] = std::thread(stage1_parallel, std::ref(q1), std::ref(q2), std::ref(q3), is_print);
    threads[1] = std::thread(stage2_parallel, std::ref(q1), std::ref(q2), std::ref(q3), is_print);
    threads[2] = std::thread(stage3_parallel, std::ref(q1), std::ref(q2), std::ref(q3), is_print);

    for (int i = 0; i < THREADS; i++)
    {
        threads[i].join();
    }
    max[0] = t1[count - 1];
    for (int i = 0; i < count; i++)
    {
       if (t2[i] - t1[i] > max[1])
           max[1] = t2[i] - t1[i];
       if (t3[i] - t2[i] > max[2])
           max[2] = t3[i] - t2[i];
       avg[0] += t1[i];
       avg[1] += (t2[i] - t1[i]);
       avg[2] += (t3[i] - t2[i]);
       time1[i] = t1[i];
       time2[i] = t2[i] - t1[i];
       time3[i] = t3[i] - t2[i];
       if (time1[i]+time2[i]+time3[i] > maxq)
           maxq = time1[i]+time2[i]+time3[i];
       if (time1[i]+time2[i]+time3[i] < minq)
           minq = time1[i]+time2[i]+time3[i];
       avgq += (time1[i]+time2[i]+time3[i]);
       sum[i] = time1[i] + time2[i] + time3[i];
       sumsys[i] = t1[i] + t2[i] + t3[i];
    }
    mins = get_min_(sumsys, count);
    maxs = get_max_(sumsys, count);
    avgs = get_avg_(sumsys, count);
    mids = get_mid_(sumsys, count);

    sort_arr(time1, count);
    sort_arr(time2, count);
    sort_arr(time3, count);
    sort_arr(sum, count);
    int ind = count / 2;
    if (count % 2 == 0)
    {
        mid[0] = (time1[ind] + time1[ind - 1]) / 2;
        mid[1] = (time2[ind] + time2[ind - 1]) / 2;
        mid[2] = (time3[ind] + time3[ind - 1]) / 2;
        midq = (sum[ind] + sum[ind - 1]) / 2;
    }
    else
    {
        mid[0] = time1[ind];
        mid[1] = time2[ind];
        mid[2] = time3[ind];
        midq = sum[ind];
    }
    for (int i = 0; i < 3; i++) {
        avg[i] /= count;
        printf("\nIn stage %d >> min = %lf, max = %lf, avg = %lf, mid = %lf\n", i + 1, min[i], max[i], avg[i], mid[i]);
    }
    avgq /= count;
    printf("\nIn all stages >> min = %lf, max = %lf, avg = %lf, mid = %lf\n", minq, maxq, avgq, midq);
    printf("\nIn system >> min = %lf, max = %lf, avg = %lf, mid = %lf\n", mins, maxs, avgs, mids);
}


void time_mes(void)
{
    int act, alg_option;

    std::cout << "\n\nВыбор алгоритма: \
                    \n\t1) Последовательный \
                    \n\t2) Конвейер \n\n";

    std::cin >> alg_option;

    std::cout << "\n\nЗамер времени: \
                    \n\t1) Разный размер матриц \
                    \n\t2) Разное кол-во матриц\n\n";

    std::cin >> act;

    if (act == 1)
    {
        int count = 0;
        size_t size_b, size_e;

        std::cout << "\nКоличество матриц >> ";
        std::cin >> count;

        std::cout << "\nНачальный размер >> ";
        std::cin >> size_b;

        std::cout << "\nКонечный размер >> ";
        std::cin >> size_e;

        if ((alg_option < 3) && (alg_option > 0))
            printf("\n\n Размер   |   Время \
                \n----------------------\n");
        else
        {
            printf("Ошибка: выбран несуществующий алгоритм!\n");
            return;
        }


        for (size_t i_size = size_b; i_size <= size_e; i_size += STEP_SIZE)
        {
            time_now = 0;

            if (alg_option == 1)
            {
                parse_linear(count, i_size, false);

                printf("  %3zu     |   %3.4f\n", i_size, time_now);
            }
            else if (alg_option == 2)
            {
                parse_parallel(count, i_size, false);

                printf("  %3zu     |   %3.4f\n", i_size, time_now);
            }
        }
    }
    else if (act == 2)
    {
        int count_b, count_e;
        size_t size;

        std::cout << "\nНачальное количество >> ";
        std::cin >> count_b;

        std::cout << "\nКонечное количество >> ";
        std::cin >> count_e;

        std::cout << "\nРазмер квадратных матриц >> ";
        std::cin >> size;

        if ((alg_option < 3) && (alg_option > 0))
            printf("\n\n Кол-во   |   Время \
                \n----------------------\n");
        else
        {
            printf("Ошибка: выбран несуществующий алгоритм!\n");
            return;
        }


        for (int i_count = count_b; i_count <= count_e; i_count += STEP_COUNT)
        {
            time_now = 0;

            if (alg_option == 1)
            {
                parse_linear(i_count, size, false);

                printf("  %4d    |   %3.4f\n", i_count, time_now);
            }
            else if (alg_option == 2)
            {
                parse_parallel(i_count, size, false);

                printf("  %4d    |   %3.4f\n", i_count, time_now);
            }
        }
    }
    else
    {
        printf("Ошибка: выбран несуществующий тип замеров!\n");
    }
}


void info_stages(void)
{
    printf("\n\nПоследовательная обработка матриц: \
            \n\tЭтап 1. Умножение матрицы самой на себя (квадрат матрицы)\
            \n\tЭтап 2. Приведение матрицы к верхнетреугольному виду \
            \n\tЭтап 3. Поиск определителя матрицы");
}
