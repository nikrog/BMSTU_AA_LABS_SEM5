import matplotlib.pyplot as plt
fig1 = plt.figure(figsize=(10, 7))
plot = fig1.add_subplot()
values = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
very_short = [1, 1, 1, 5/6, 5/6, 5/6, 4/6, 1/6, 0, 0, 0, 0, 0, 0, 0]
short = [0, 0, 0, 1/6, 1/6, 1/6, 2/6, 4/6, 4/6, 0, 0, 0, 0, 0, 0]
average = [0, 0, 0, 0, 0, 0, 0, 1/6, 2/6, 1, 3/6, 1/6, 0, 0, 0]
high = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/6, 5/6, 1/6, 0, 0]
very_high = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/6, 5/6, 1, 1]

values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
very_low = [1, 1/7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
low = [0, 6/7, 6/7, 6/7, 4/7, 3/7, 2/7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
average = [0, 0, 1/7, 1/7, 3/7, 4/7, 4/7, 6/7, 6/7, 6/7, 3/7, 2/7, 1/7, 0, 0, 0, 0, 0, 0, 0, 0]
high = [0, 0, 0, 0, 0, 0, 1/7, 1/7, 1/7, 1/7, 3/7, 4/7, 5/7, 6/7, 6/7, 4/7, 2/7, 1/7, 1/7, 0, 0]
very_high = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/7, 1/7, 1/7, 1/7, 1/7, 3/7, 5/7, 6/7, 6/7, 1, 1]

plot.plot(values, very_low, label = "«Очень низкая»")
plot.plot(values, low, ":", label="«Низкая»", marker="o")
plot.plot(values, average, "--", label="«Средняя»", marker="v")
plot.plot(values, high, "--", label="«Высокая»", marker="^")
plot.plot(values, very_high, "--", label="«Очень высокая»", marker="s")

plt.legend()
plt.grid()
plt.title("Графики функций принадлежности числовых значений \nпеременной термам, описывающим группы значений лингвистической переменной")
plt.ylabel("μ")
plt.xlabel("Трансферная стоимость, миллионов евро")

plt.show()