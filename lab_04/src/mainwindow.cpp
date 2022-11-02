#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>

QImage image = QImage(WIN_X, WIN_Y, QImage::Format_RGB32);

MainWindow::MainWindow(QWidget *parent):
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    image.fill(16777215);

    QGraphicsScene *scene = new QGraphicsScene(this);
    ui->graphicsView->setScene(scene);
    ui->graphicsView->setAlignment(Qt::AlignTop | Qt::AlignLeft);

    scene->setSceneRect(0, 0, WIN_X, WIN_Y);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_clean_clicked()
{
    image.fill(16777215);
    ui->graphicsView->scene()->addPixmap(QPixmap::fromImage(image));
}

void MainWindow::read_parallel(int &type_parallel)
{
    if (ui->no_parallel->isChecked())
    {
        type_parallel = NO_PARALLEL;
    }
    else if (ui->parallel->isChecked())
    {
        type_parallel = PARALLEL;
    }
}


request_t MainWindow::init(void)
{
    request_t request;
    read_parallel(request.algorithm);
    request.scene = ui->graphicsView->scene();

    return request;
}


void MainWindow::on_beam_clicked()
{
    request_t request = init();
    request.is_draw = true;
    spektr_t settings = { ui->beam_entry->value(), ui->threads_entry->value() };

    if (ui->beam_entry->value() == 0 || ui->threads_entry->value() == 0)
    {
        QMessageBox::critical(this, "Error", "Invalid values!");
        return;
    }

    if (request.algorithm == NO_PARALLEL)
        calculate_beam_no_parallel(request, settings);
    else if (request.algorithm == PARALLEL)
        calculate_beam_parallel(request, settings);

    request.scene->addPixmap(QPixmap::fromImage(image));
}


void MainWindow::on_time_mes_btn_clicked()
{
    request_t request = init();
    request.is_draw = false;

   spektr_t settings = { ui->beam_entry->value() };

    if (ui->beam_entry->value() == 0)
    {
        QMessageBox::critical(this, "Error", "Invalid values!");
        return;
    }

    if (request.algorithm == NO_PARALLEL)
    {
        double res_time = time_mes_no_parallel(request, settings);

        std::cout << "Time (no parallel): " << res_time << " seconds"<<std::endl;
    }
    else if (request.algorithm == PARALLEL)
    {
        std::cout << "   Num of threads   |      Time     " << std::endl;
        std::cout << " -----------------------------------" << std::endl;

        for (int threads = 1; threads <= MAX_THREADS; threads*=2)
        {
            settings.threads_count = threads;

            double res_time = time_mes_parallel(request, settings);

            printf("        %-3d         |    %-.6f\n", settings.threads_count, res_time);
        }
    }

    std::cout << "\n ======= Time measuring <ENDED> ======= \n " << std::endl;

    request.scene->addPixmap(QPixmap::fromImage(image));
}


void MainWindow::on_time_mes_btn_dif_d_clicked()
{
    request_t request = init();
    request.is_draw = false;

    spektr_t settings = { ui->beam_entry->value(), ui->threads_entry->value() };

    if (ui->beam_entry->value() == 0 || ui->threads_entry->value() == 0)
    {
        QMessageBox::critical(this, "Error", "Invalid values!");
        return;
    }

    std::cout << "       Len of beam      |     Time    " << std::endl;
    std::cout << " -------------------------------------" << std::endl;

    double res_time;

    for (int diam = MIN_DIAM; diam <= MAX_DIAM; diam += DIAM_STEP)
    {
        settings.d = diam;

        if (request.algorithm == NO_PARALLEL)
            res_time = time_mes_no_parallel(request, settings);
        else if (request.algorithm == PARALLEL)
            res_time = time_mes_parallel(request, settings);

        printf("        %-5d         |    %-.6f\n", diam, res_time);
    }

    std::cout << "\n ======= Time measuring <ENDED> ======= \n " << std::endl;

    request.scene->addPixmap(QPixmap::fromImage(image));
}
