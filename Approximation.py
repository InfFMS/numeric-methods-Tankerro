import matplotlib.pyplot as plt
import numpy as np
import math

Xdata1 = np.arange(0, math.pi, 0.001)
Xdata2 = np.arange(-math.pi/2, math.pi/2, 0.001)
Xdata3 = np.arange(-2, 2, 0.001)


def f1_1(x):
    return math.sin(2*x) + 1
def f1_2(x):
    return -0.2*x**2+0.5

def f2_1(x):
    return math.cos(x) + 1.2
def f2_2(x):
    return -0.5*x**2+0.7

def f3_1(x):
    return math.e**(-1*(x+1)**2)+math.e**(-1*(x-1)**2)+0.5
def f3_2(x):
    return -0.3*x**2


def f4_1(x):
    return math.e**(-1*x**2)+0.5
def f4_2(x):
    return -0.2*math.sin(3*x)-0.5

def f5_1(x):
    return math.e**(-1*x**2)+1
def f5_2(x):
    return -0.3*x**3+0.5

Ydata1_1 = []
Ydata1_2 = []
for i in Xdata1:
    Ydata1_1.append(f1_1(i))
    Ydata1_2.append(f1_2(i))
Ydata1_1 = np.array(Ydata1_1)
Ydata1_2 = np.array(Ydata1_2)

Ydata2_1 = []
Ydata2_2 = []
for i in Xdata2:
    Ydata2_1.append(f2_1(i))
    Ydata2_2.append(f2_2(i))
Ydata2_1 = np.array(Ydata2_1)
Ydata2_2 = np.array(Ydata2_2)

Ydata3_1 = []
Ydata3_2 = []
for i in Xdata3:
    Ydata3_1.append(f3_1(i))
    Ydata3_2.append(f3_2(i))
Ydata3_1 = np.array(Ydata3_1)
Ydata3_2 = np.array(Ydata3_2)

Ydata4_1 = []
Ydata4_2 = []
for i in Xdata3:
    Ydata4_1.append(f4_1(i))
    Ydata4_2.append(f4_2(i))
Ydata4_1 = np.array(Ydata4_1)
Ydata4_2 = np.array(Ydata4_2)

Ydata5_1 = []
Ydata5_2 = []
for i in Xdata3:
    Ydata5_1.append(f5_1(i))
    Ydata5_2.append(f5_2(i))
Ydata5_1 = np.array(Ydata5_1)
Ydata5_2 = np.array(Ydata5_2)

def calc(array, func):
    x = array[0]
    y1 = func(x)
    sum = 0
    while x < array[len(array)-1]:
        x += 0.001
        y2 = func(x)
        sum += 0.5 * (y1 + y2) * 0.001
        y1 = y2
    return sum


print(abs(calc(Xdata1, f1_1) - calc(Xdata1, f1_2)))
print(abs(calc(Xdata2, f2_1) - calc(Xdata2, f2_2)))
print(abs(calc(Xdata3, f3_1) - calc(Xdata3, f3_2)))
print(abs(calc(Xdata3, f4_1) - calc(Xdata3, f4_2)))
print(abs(calc(Xdata3, f5_1) - calc(Xdata3, f5_2)))