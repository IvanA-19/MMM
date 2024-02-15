import numpy as np


n = 19
e = 10 ** (-4)
w = 1.2432
x2 = np.zeros(n)
x1 = np.zeros(n + 1)
x0 = np.ones(n)


def get_matrix(n):
    a = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    a[0][0] = 1
    f = [1]

    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j and i != 0:
                a[i][j] = -2
            elif (j == i + 1 or j == i - 1) and i != 0:
                a[i][j] = 1

    a[len(a) - 1][0] = 1
    a[len(a) - 1][len(a[len(a) - 1]) - 1] = 1
    for i in range(1, len(a[len(a) - 1]) - 1):
        a[len(a) - 1][i] = 2

    for i in range(2, n + 1):
        f.append(2 / (i**2))
    f.append(-n / 3)
    return a, f


A = np.array(get_matrix(n)[0])
f = np.array(get_matrix(n)[1])


def Gauss_method():
    for i in range(n):
        b = n - 1 - i
        for j in range(i, n):
            m = n - 1 - j
            if b != m:
                f[m] = f[m] - ((f[b] * A[m][b]) / A[b][b])
                A[m] = (A[m] - (A[b] * A[m][b]) / A[b][b])

    X = np.zeros(n + 1)
    for i in range(n):
        X[i] = f[i] / A[i][i]

    normVector = np.linalg.norm(np.matmul(A, X) - f)
    print(f"Норма вектора невязки методом Гаусса = {normVector} ")

    numOfConditionality = np.linalg.norm(A) * np.linalg.norm(np.linalg.inv(A))
    print(f'Число обусловленности матрицы А = {numOfConditionality}')

    b = np.linalg.eig(A)
    print(f"L min = {min(b[0])}")
    print(f"L max = {max(b[0])}")


def PVR_method():
    while all(abs(np.matmul(A, x1) - f)) > e:
        for i in range(n):
            res = 0
            for j in range(n):
                if i != j:
                    res += A[i][j] * x0[j]
            x1[i] = (f[i] - res) / A[i][i]
            x2[i] = x0[i]
            x0[i] = x1[i]

    for i in range(n):
        x1[i] = (1 - w) * x2[i] + w * x1[i]

    normVector = np.linalg.norm(np.matmul(A, x1) - f)
    print(f"Норма вектора невязки методом ПВР = {normVector}")


Gauss_method()
PVR_method()
