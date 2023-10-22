import numpy as np
import numpy.linalg as la
import copy
import sympy as sp

# Starter pack function;
def gauss(A_in, b_in):

    A = copy.deepcopy(A_in)
    b = copy.deepcopy(b_in)
    size = b.shape[0]

    for k in range(0, size - 1):
        for i in range(k + 1, size):
            if A[i, k] != 0:
                c = A[i, k] / A[k, k]
                A[i, k + 1:size] = A[i, k + 1:size] - c * A[k, k + 1:size]
                b[i] = b[i] - c * b[k]

    # обратный ход
    for k in range(size - 1, -1, -1):
        save = b[k]
        for j in range(k + 1, size):
            save -= A[k, j] * b[j]
        b[k] = save / A[k, k]
    return b

# Function, that initializes L, U matrix elements;
def ElemInitializer(A, L, U, size):

    for i in range(size):
        for j in range(size):
            if i <= j:
                U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
            if i > j:
                L[i, j] = (A[i, j] - np.dot(L[i, :j], U[:j, j])) / U[j, j]

# Function, that create unit matrix;
def UnitMatrixCreator(size):

    UnitMatrix = [[0] * size for index in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            if i == j:
                UnitMatrix[i][j] = 1.
    return UnitMatrix

# Function, that lays out matrix A into 2 matrix: L & U;
def LUInitializer(A_in):

    A = copy.deepcopy(A_in)
    size = A.shape[0]

    L = np.array(UnitMatrixCreator(size))
    U = np.array([[0.] * size for index in range(size)])
    ElemInitializer(A, L, U, size)
    return L, U

# Function, that can get solve of equation system;
def GetSolve(A_in, b_in, L_in, U_in):

    A = copy.deepcopy(A_in)
    b = copy.deepcopy(b_in)
    L = copy.deepcopy(L_in)
    U = copy.deepcopy(U_in)

    y = gauss(L, b)
    solve = gauss(U, y)

    return solve

# Main function;
def main():

    A = np.array([[1., 1., 1.], [0., 1., 2.], [7., 1., 4.]])
    b = np.array(UnitMatrixCreator(A.shape[0]))

    L, U = LUInitializer(A)
    solve = GetSolve(A, b, L, U)
    BackA = np.zeros_like(A)
    for i in range(A.shape[0]):
        BackA[:, i] = gauss(U, gauss(L,
                            np.array(UnitMatrixCreator(A.shape[0]))[:, i]))

    print(f"numpy.linalg.inv:\n{np.linalg.inv(A)}\n\n")
    print(f"(LU)^(-1):\n{BackA}")

main()