import numpy as np
import matplotlib.pyplot as plt


T = 3
N = 31
h = T/(N-1)
x_teor = np.linspace(0,T,(N-1)*100+1)
x = np.linspace(0,T,N)
l = -1e6
u = np.zeros(N)


#implicit  Euler method
def im_euler(u, l, h, N):
    for i in range(0, N - 1):
        u[i + 1] = (u[i] - h * (l * np.cos((i + 1) * h) + np.sin((i + 1) * h))) / (1 - l * h)

#trapezoidal method
def trapezoidal(u, l, h, N):
    for i in range(0, N - 1):
        free = l * (np.cos((i + 1) * h) + np.cos(i * h) + (np.sin((i + 1) * h) + np.sin(i * h)))
        u[i + 1] = (u[i] * (1 + l * h / 2) - h / 2 * free) / (1 - l * h / 2)



figure, axis = plt.subplots(2, 2)

im_euler(u, l, h, N)
u[0] = 1
axis[0, 0].plot(x_teor, np.cos(x_teor), color='g', label='exact')
axis[0, 0].plot(x, u, 'ro', label='implicit Euler')
u[0] = 1.5
axis[0, 1].plot(x_teor, np.cos(x_teor), color='g', label='exact')
axis[0, 1].plot(x, u, 'ro', label='implicit Euler')



trapezoidal(u, l, h, N)
u[0] = 1
axis[1, 0].plot(x_teor, np.cos(x_teor), color='g', label='exact')
axis[1, 0].plot(x, u, 'ro', label='trapezoidal')
u[0] = 1.5
axis[1, 1].plot(x_teor, np.cos(x_teor), color='g', label='exact')
axis[1, 1].plot(x, u, 'ro', label='trapezoidal')

plt.show()