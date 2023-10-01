import math

import matplotlib.pyplot as plt

h = 0.01
LIMIT = 10 ** 5

# Directional difference;
def DirDiff(MathFunc, DiffMathFunc, x0, h):
    return abs(((MathFunc(x0 + h) - MathFunc(x0)) / h) - DiffMathFunc(x0))

# Central difference;
def CenterDiff(MathFunc, DiffMathFunc, x0, h):
    return abs(((MathFunc(x0 + h) - MathFunc(x0 - h)) /(2 * h)) - DiffMathFunc(x0))

# Creating of graphic DiffFunc(h);
def DirDiffGraphic(DiffFunc, h):

    XDiff = []
    YDiff = []
    for i in range(LIMIT):
        hSave = h + 0.01
        h = hSave
        XDiff.append(h)
        YDiff.append(DiffFunc(math.sin, math.cos, 1, h) / DiffFunc(math.sin, math.cos, 1, h / 2))

    XDiff = list(map(math.log2, XDiff))
    YDiff = list(map(math.log2, YDiff))
    plt.plot(XDiff, YDiff)

DirDiffGraphic(DirDiff, h)
DirDiffGraphic(CenterDiff, h)
plt.show()