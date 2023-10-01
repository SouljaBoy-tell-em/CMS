import math
import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as LA

mStart =  2
mMax   = 15

# Create Vandermonde matrix;
def CreateVanderMatr(Xstart, N):
    list = np.array(range(Xstart, N - 1))
    return np.transpose(np.fliplr(np.vander(list, N)))

# Creating of graphic mu(m);
def CreateGraphic():
    listM = []
    listMu = []
    for i in range(mStart, mMax):
        listM.append(i)
        listMu.append(LA.cond(CreateVanderMatr(-1, i)))
    listMu = list(map(math.log, listMu))
    plt.plot(listM, listMu)

CreateGraphic()
plt.show()

