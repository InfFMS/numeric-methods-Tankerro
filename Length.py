import matplotlib.pyplot as plt
import numpy as np
import math

def first_cos(x):
    return math.cos(x)

def second_cos(x):
    return math.cos(x) + 0.1*x**2

def third_cos(x):
    return -math.tanh(x-math.pi/2)

def fourth_cos(x):
    return -0.2*(x-math.pi)**3 + 0.5*(x - math.pi)**2 + 1

X3, axs = plt.subplots(1, 4, figsize=(10, 4))

Xdata = np.arange(0, math.pi, 0.01)
Ydata1 = []
for i in Xdata:
    Ydata1.append(first_cos(i))
Ydata1 = np.array(Ydata1)
axs[0].plot(Xdata, Ydata1)

Ydata2 = []
for i in Xdata:
    Ydata2.append(second_cos(i))
Ydata2 = np.array(Ydata2)
axs[1].plot(Xdata, Ydata2)

Ydata3 = []
for i in Xdata:
    Ydata3.append(third_cos(i))
Ydata3 = np.array(Ydata3)
axs[2].plot(Xdata, Ydata3)

Ydata4 = []
for i in Xdata:
    Ydata4.append(fourth_cos(i))
Ydata4 = np.array(Ydata4)
axs[3].plot(Xdata, Ydata4)

i = 0
j = 1
def find_curve_len(x, y):
    sum = 0
    i = 0
    j = 0
    while i < len(x)-1 and j < len(y)-1:
        sum += ((x[i+1]-x[i])**2 + (y[j+1]-y[j])**2)**(1/2)
        i += 1
        j += 1
    return sum

print(find_curve_len(Xdata, Ydata1))
print(find_curve_len(Xdata, Ydata2))
print(find_curve_len(Xdata, Ydata3))
print(find_curve_len(Xdata, Ydata4))

plt.show()