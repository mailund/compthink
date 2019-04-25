import numpy as np

x = 'baz'
y = 'fbar'


def build_edit_table(x, y):
    n, m = len(x), len(y)
    D = np.zeros((n + 1, m + 1))

    # base cases
    for i in range(n + 1):
        D[i,0] = i
    for j in range(m + 1):
        D[0,j] = j

    # recursion
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i,j] = min(
                D[i - 1, j - 1] + int(x[i - 1] != y[j - 1]),
                D[i, j - 1] + 1,
                D[i - 1, j] + 1
            )

    return D

def edit_dist(x, y):
    D = build_edit_table(x, y)
    n, m = len(x), len(y)
    return D[n,m]

def backtrack_(D, x, y, i, j, path):
    if i == 0:
        path.extend('D' * j)
        return
    if j == 0:
        path.extend('I' * i)
        return

    left = D[i, j - 1] + 1
    diag = D[i - 1, j - 1] + int(x[i - 1] != y[j - 1])
    up = D[i - 1, j] + 1

    dist = left
    op = 'D'
    if diag < dist:
        op = 'X' if x[i - 1] != y[j - 1] else '='
        dist = diag
    if up < dist:
        op = 'I'

    path.append(op)
    if op == 'D':
        backtrack_(D, x, y, i, j - 1, path)
    if op in ('=','X'):
        backtrack_(D, x, y, i - 1, j - 1, path)
    if op == 'I':
        backtrack_(D, x, y, i - 1, j, path)

def backtrack(D, x, y):
    n, m = len(x), len(y)
    path = []
    backtrack_(D, x, y, n, m, path)
    path.reverse()
    return ''.join(path)

D = build_edit_table(x, y)
print(backtrack(D, x, y))
