import math
import numpy as np
import matplotlib.pyplot as plt

mStart =  2
mMax   = 25

# Create Vandermonde matrix;
def CreateVanderMatr(l, m):
    list = np.array(range(-l, m + 1))
    return np.transpose(np.fliplr(np.vander(list, l + m + 1)))

# Initialize right column and getting solves to a system of equations;
def GetSolve(VanderMatr, N):
    b = [0] * (N + 1)
    b[1] = 1
    return np.linalg.solve(VanderMatr, b)

# There is sum formula and function return meaning of difference between derivative
# and this sum as a result;
def SumOfFunctionValues(MathFunc, DiffMathFunc, VanderMatrSolve, Xmin, Xmax, l, m):
    h = (Xmax - Xmin) / (l + m)
    MathFuncResult = 0
    for i in range(-l, m + 1):
        MathFuncResult += VanderMatrSolve[i + l] * MathFunc((Xmin + l * h) + i * h)
    MathFuncResult /= h
    return abs(MathFuncResult - DiffMathFunc(Xmin + l * h))

# Getting of fluctuation between 2 points: Xmin, Xmax;
def Result(l, m, Xmin, Xmax):
    VanderMatr = CreateVanderMatr(l, m)
    VanderMatrSolve = GetSolve(VanderMatr, l + m)
    fluctuation = SumOfFunctionValues(math.sin, math.cos, VanderMatrSolve, Xmin, Xmax, l, m)
    return fluctuation

# Creating of graphic fluctuation(N);
def CreateGraphic():
    listM = []
    listFluctuation = []

    for i in range(mStart, mMax):
        listM.append(i)
        listFluctuation.append(Result(1, i, 0, 5))
    listFluctuation = list(map(math.log, listFluctuation))
    plt.plot(listM, listFluctuation)

CreateGraphic()
plt.show()