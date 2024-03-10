import matplotlib.pyplot as plt
import numpy as np


T = 1
N = 1001
h = 0
x = 0
x_teor = 0
l = -200
u = np.zeros(1)
u[0] = 1

#explicit Euler method
def ex_euler(u, l, h, N):
    for i in range(0, N - 1):
        u[i + 1] = (1 + l * h) * u[i]

#implicit Euler method
def im_euler(u, l, h, N):
    for i in range(0, N - 1):
        u[i+1] = u[i] / (1 - l * h)

def Initializer(n):
    global N, h, x, x_teor, u
    T = 1
    N = n
    h = T / (N - 1)
    x = np.linspace(0, T, N)
    x_teor = np.linspace(0, T, (N - 1) * 100 + 1)
    l = -200
    u = np.zeros(N)
    u[0] = 1


figure, axis = plt.subplots(2, 3)
axis[0, 0].axis([0, 0.1, -1.1, 1.1])
axis[0, 1].axis([0, 0.1, -1.1, 1.1])
axis[0, 2].axis([0, 0.1, -1.1, 1.1])
axis[1, 0].axis([0, 0.1, -1.1, 1.1])
axis[1, 1].axis([0, 0.1, -1.1, 1.1])
axis[1, 2].axis([0, 0.1, -1.1, 1.1])


Initializer(1001)
ex_euler(u, l, h, N)
axis[0, 0].plot(x_teor, np.exp(l * x_teor), color='g', label='exact')
axis[0, 0].plot(x, u, 'ro', label='explicit Euler')
axis[0, 0].legend("")

Initializer(101)
ex_euler(u, l, h, N)
axis[0, 1].plot(x_teor, np.exp(l * x_teor), color='g', label='exact')
axis[0, 1].plot(x, u, 'ro', label='explicit Euler')

Initializer(100)
ex_euler(u, l, h, N)
axis[0, 2].plot(x_teor, np.exp(l * x_teor), color='g', label='exact')
axis[0, 2].plot(x, u, 'ro', label='explicit Euler')



Initializer(1001)
im_euler(u, l, h, N)
axis[1, 0].plot(x_teor, np.exp(l * x_teor), color='g', label='exact')
axis[1, 0].plot(x, u, 'ro', label='implicit Euler')

Initializer(101)
im_euler(u, l, h, N)
axis[1, 1].plot(x_teor, np.exp(l * x_teor), color='g', label='exact')
axis[1, 1].plot(x, u, 'ro', label='implicit Euler')

Initializer(100)
im_euler(u, l, h, N)
axis[1, 2].plot(x_teor, np.exp(l * x_teor), color='g', label='exact')
axis[1, 2].plot(x, u, 'ro', label='implicit Euler')

plt.show()
