import numpy as np

A = np.array([
    [15, -5, 1, 1.1],
    [0, 7, 2, -1],
    [2, -1, 9, -1],
    [1, 1.1, -1, -6]
], dtype=float)

b = np.array([1,1,1,1], dtype=float)

x = np.array([2.,1.,1.,1.])

for k in range(10):
    x[0] = (1 +5*x[1] - x[2] -1.1*x[3]) / 15
    x[1] = (1 -2*x[2] + x[3]) / 7
    x[2] = (1 -2*x[0] + x[1] + x[3]) / 9
    x[3] = (x[0] +1.1*x[1] - x[2] -1) / 6

norm = np.linalg.norm(x)
print(norm)
