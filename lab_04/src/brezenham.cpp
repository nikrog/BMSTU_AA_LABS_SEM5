#include "brezenham.h"


extern QImage image;


int sign(const int &number)
{
    if (number > 0)
    {
        return 1;
    }
    else if (number < 0)
    {
        return -1;
    }

    return 0;
}

void swap(int &dx, int &dy)
{
    int t;
    t = dx;
    dx = dy;
    dy = t;
}

static void draw_pixel(const request_t &request, int x, int y)
{
    image.setPixel(x, y, request.color.rgb());
}


void breshenham_float(const request_t &request, const point_t &pt1, const point_t &pt2)
{
    int dx = abs(pt2.x - pt1.x);
    int dy = abs(pt2.y - pt1.y);

    int sx = sign(pt2.x - pt1.x);
    int sy = sign(pt2.y - pt1.y);

    int change = 0;

    if (dy > dx)
    {
        swap(dx, dy);
        change = 1;
    }

    double m = (double)dy / (double)dx;
    double e = m - 0.5;

    int x = pt1.x;
    int y = pt1.y;

    std::mutex mut;

    for (int i = 0; i < dx; i++)
    {
        if (request.is_draw)
        {
            mut.lock();
            draw_pixel(request, x, y);
            mut.unlock();
        }

        if (e >= 0)
        {
            if (change == 0)
            {
                y += sy;
            }
            else
            {
                x += sx;
            }

            e -= 1;
        }
        if (change == 0)
        {
             x += sx;
        }
        else
        {
            y += sy;
        }

        e += m;
    }

}


void calculate_beam_no_parallel(const request_t &request, const spektr_t &params)
{
    int spektr = 360;

    point_t pt1, pt2;
    pt1.x = WIN_X / 2;
    pt1.y = WIN_Y / 2;

    for (int i = 0; i < spektr; i += 1)
    {
        pt2.x = cos(i * PI / 180) * params.d + WIN_X / 2;
        pt2.y = sin(i * PI / 180) * params.d + WIN_Y / 2;

        // Round for Bresenham float
        pt1.x = round(pt1.x);
        pt1.y = round(pt1.y);
        pt2.x = round(pt2.x);
        pt2.y = round(pt2.y);


        calculate_line(request, pt1, pt2);
    }
}


void calculate_part_beam(const request_t &request, const spektr_t &params, int thread_ind)
{
    int spektr = 360;
    int sector_in_thread = spektr / params.threads_count;
    int part_ind = thread_ind * sector_in_thread;

    if (thread_ind + 1 == params.threads_count)
    {
        sector_in_thread += (spektr - sector_in_thread * params.threads_count);
    }

    point_t pt1, pt2;
    pt1.x = WIN_X / 2;
    pt1.y = WIN_Y / 2;

    for (int i = part_ind; i < part_ind + sector_in_thread; i += 1)
    {

        pt2.x = cos(i * PI / 180) * params.d + WIN_X / 2;
        pt2.y = sin(i * PI / 180) * params.d + WIN_Y / 2;

        // Round for Bresenham float
        pt1.x = round(pt1.x);
        pt1.y = round(pt1.y);
        pt2.x = round(pt2.x);
        pt2.y = round(pt2.y);

        calculate_line(request, pt1, pt2);
    }
}


void calculate_beam_parallel(const request_t &request, const spektr_t &params)
{
    std::vector<std::thread> threads(params.threads_count);

    for (int i = 0; i < params.threads_count; i++)
    {
        threads[i] = std::thread(calculate_part_beam, request, params, i);
    }

    for (int i = 0; i < params.threads_count; i++)
    {
        threads[i].join();
    }
}


void calculate_line(const request_t &request, const point_t &pt1, const point_t &pt2)
{
    breshenham_float(request, pt1, pt2);
}


double time_mes_no_parallel(const request_t &request, const spektr_t &params)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double res_time = 0;

    for (int i = 0; i < ITERATIONS; i++)
    {
        time_start = std::chrono::system_clock::now();
        calculate_beam_no_parallel(request, params);
        time_end = std::chrono::system_clock::now();

        res_time += (std::chrono::duration_cast<std::chrono::nanoseconds>
            (time_end - time_start).count());
    }

    res_time /= ITERATIONS;

    return res_time / 1e9;
}


double time_mes_parallel(const request_t &request, const spektr_t &params)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double res_time = 0;

    for (int i = 0; i < ITERATIONS; i++)
    {
        time_start = std::chrono::system_clock::now();
        calculate_beam_parallel(request, params);
        time_end = std::chrono::system_clock::now();

        res_time += (std::chrono::duration_cast<std::chrono::nanoseconds>
            (time_end - time_start).count());
    }

    res_time /= ITERATIONS;

    return res_time / 1e9;
}
