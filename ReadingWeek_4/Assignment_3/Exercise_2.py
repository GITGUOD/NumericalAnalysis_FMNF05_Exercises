import numpy as np

A = np.array([
    [3, 1, 1, 0],
    [1, 6, 3, -1],
    [6, 0, 9, -2],
    [1, 0, -1, -7]
], dtype=float)

b = np.array([10,1,1,1], dtype=float)

x = np.array([0.,1.,1.,0.])   # x(0)

for k in range(25):
    x_new = np.zeros_like(x)
    
    x_new[0] = (10 - x[1] - x[2]) / 3
    x_new[1] = (1 - x[0] - 3*x[2] + x[3]) / 6
    x_new[2] = (1 - 6*x[0] + 2*x[3]) / 9
    x_new[3] = (x[0] - x[2] - 1) / 7
    
    x = x_new

norm = np.linalg.norm(x)
print(norm)
