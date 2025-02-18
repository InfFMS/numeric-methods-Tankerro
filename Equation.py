import matplotlib.pyplot as plt
import numpy as np
import math

X3, axs = plt.subplots(1, 5, figsize=(10, 4))  # 1 ряд, 3 столбца

Xdata = np.arange(-2, 2, 0.01)

#ось X
axs[0].plot(Xdata, np.array([0]*400))


# решебник
def solve(a, b, f, eps):
    while b - a >= 2*eps:
        x = (b + a) / 2
        if f(a)*f(x) <= 0:
           b = x
        else:
            a = x
    print(x)
    return x

# функция (x**3)-x+1
def funcx3(x):
    a = (x**3)-x+1
    return a

# решение
YdataX3 = funcx3(Xdata) # (x**3)-x+1
axs[0].plot(Xdata, YdataX3)
AnsX3 = solve(-5, 5, funcx3, 0.001)
axs[0].scatter([AnsX3], [funcx3(AnsX3)])

def funcx3_full(x):
    a = (x**3)-(x**2)-9*x+9
    return a

Xdata = np.arange(-5, 5, 0.01)
axs[1].plot(Xdata, np.array([0]*1000))
YdataX3_full = funcx3_full(Xdata)
axs[1].plot(Xdata, YdataX3_full)
AnsX3_full1 = solve(-5, 5, funcx3_full, 0.001)
AnsX3_full2 = solve(0, 2, funcx3_full, 0.001)
AnsX3_full3 = solve(2, 4, funcx3_full, 0.001)
axs[1].scatter([AnsX3_full1], [funcx3_full(AnsX3_full1)])
axs[1].scatter([AnsX3_full2], [funcx3_full(AnsX3_full2)])
axs[1].scatter([AnsX3_full3], [funcx3_full(AnsX3_full3)])

def exp(x):
    a = (x**2)-math.e**x
    return a

Xdata = np.arange(-5, 5, 0.01)
axs[2].plot(Xdata, np.array([0]*1000))
YdataExp = exp(Xdata)
axs[2].plot(Xdata, YdataExp)
AnsExp = solve(-1, 1, exp, 0.001)
axs[2].scatter([AnsExp], [exp(AnsExp)])


# функция не работает сделал через цикл
def ln(x):
    a = 5*x - 6*math.log1p(x) - 7
    return a

YdataLn = []
Xdata = np.arange(0, 5, 0.01)
for i in Xdata:
    YdataLn.append(ln(i))
YdataLn = np.array(YdataLn)
axs[3].plot(Xdata, np.array([0]*500))
axs[3].plot(Xdata, YdataLn)
AnsLn = solve(0, 5, ln, 0.001)
axs[3].scatter([AnsLn], [ln(AnsLn)])

def cos(x):
    a = math.cos(x) + 2*x - 3
    return a

Xdata = np.arange(0, 5, 0.01)

YdataCos = []
for i in Xdata:
    YdataCos.append(cos(i))
YdataCos = np.array(YdataCos)
axs[4].plot(Xdata, np.array([0]*500))
axs[4].plot(Xdata, YdataCos)

AnsCos = solve(1, 2, cos, 0.001)
axs[4].scatter([AnsCos], [cos(AnsCos)])

plt.show()

