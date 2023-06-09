import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# данная функция решает уравнение (8) из документа численно
def eiler (y0, deriv1y0, tau, t0, tend, x0):
    # создание необходимых констант и списков
    y = []
    y.append(y0)
    deriv1y = []
    deriv1y.append(deriv1y0)
    t = t0
    y1 = y0
    deriv1y1 = deriv1y0
    x = []
    x.append(x0)
    flag = 1
    tsum = [0]

    # цикл, вычисляющий значение y[i] и x[i] в каждый элементарного времени
    for i in range(int((tend - t0)/tau) + 1):
        # проверка на прохождение нижней точки маятником
        if y[i] > -5:
            # расписываю уравнение по частям, чтобы не запутаться
            a0 = -y1 * (deriv1y1**2)
            a2 = a0/(25-(y1**2)) - (9.81 + 0.05 * math.sin(2 * 3.14 * t)) * (25-(y1**2)) / 25
            # deriv2y = (-((float(y[i]) * (float(deriv1y[i])) ** 2 )) - (9.81 + 0.05 * math.sin(2 * 3.14 * t)) * (1 - (float(y[i]) ** 2)**2 / 25)) * tau
            # интегрирование функции
            app1 = deriv1y1 + a2 * tau
            deriv1y.append(app1)
            app2 = y1 + (deriv1y1 * tau)
            y.append(app2)
            deriv1y1 = deriv1y1 + (a2 * tau)
            y1 = y1 + deriv1y1 * tau
            # вывод иксов
            v = math.sqrt(abs(25 - y1 ** 2)) * (-1)**(flag-1)
            x.append(v)
        else:
            flag = flag + 1
            deriv1y2 = (-1) * deriv1y1
            a0 = -y1 * (deriv1y2**2)
            a2 = a0/(25-(y1**2)) - (9.81 + 0.05 * math.sin(2 * 3.14 * t)) * (25-(y1**2)) / 25
            # deriv2y = (-((float(y[i]) * (float(deriv1y[i])) ** 2 )) - (9.81 + 0.05 * math.sin(2 * 3.14 * t)) * (1 - (float(y[i]) ** 2)**2 / 25)) * tau
            app1 = deriv1y2 + a2 * tau
            deriv1y.append(app1)
            app2 = y1 + (deriv1y2 * tau)
            y.append(app2)
            deriv1y1 = deriv1y2 + (a2 * tau)
            y1 = y1 + deriv1y2 * tau
            v = math.sqrt(abs(25-y1**2))
            b = v * (-1)
            x.append(b)
            # deriv2y = ((((-25*(y[i])*((deriv1y[i])**2)/((25-((y[i])**2))**2)) - 9.81 - 0.05 * math.sin(2 * 3.14 * t)) * (25-((y[i])**2))) /25 * tau)
        t = t + tau
        tsum.append(t)
    return y, x, tsum

y1, x1, tall = eiler(-4, -1, 0.1, 0, 100, 3)
s = []

# получение данных для графика x^2+y^2
for k in range(len(y1)):
    y11 = y1[k]
    x11 = x1[k]
    s.append(math.sqrt(x11**2+y11**2))
fig, ax = plt.subplots()
ax.plot(tall,s)
plt.show()

# построение разных графиков
fig1, ax = plt.subplots()
ax.plot(tall,x1)
plt.show()

fig2, ax = plt.subplots()
ax.plot(tall,y1)
plt.show()

# вывод результатов численного решения
print(eiler(-4, -1, 0.01, 0, 2, 3))
print(eiler(-4, -1, 0.1, 0, 100, 3))
