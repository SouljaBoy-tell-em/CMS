import numpy as np
import numpy.linalg as la
import copy

# Starter pack updated;
def gauss(A_in, b_in):

    A = copy.deepcopy(A_in)
    b = copy.deepcopy(b_in)
    size = b.size

    for k in range(0, size - 1):
        max = np.argmax(np.abs(A[k:size, k])) + k
        if max != k:
            A[k, max] = A[max, k]
            b[k, max] = b[max, k]

        for i in range(k + 1, size):
            if A[i, k] != 0:
                c = A[i, k] / A[k, k]
                A[i, k:size] = A[i, k:size] - c * A[k, k:size]
                b[i] = b[i] - c * b[k]

    # обратный ход
    for k in range(size - 1, -1, -1):
        b[k] = (b[k] - np.dot(A[k, k + 1:size], b[k + 1:size])) / A[k, k]

    return b

# Main function;
def main():

    A1 = np.array([[1e-16, 1., -1.], [-1., 2., -1.], [2., -1., 0.]])
    b1 = np.array([0., 0., 1.])
    A2 = np.array([[1e-16, 1., -1.], [-1., 2., -1.], [2., -1., 0.]])
    b2 = np.array([0., 0., 1.])

    print(f"solve1:\n{la.solve(A1, b1)}")
    print(f"solve2:\n{la.solve(A2, b2)}")

main()