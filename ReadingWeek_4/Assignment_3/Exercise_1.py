import numpy as np

def f(x):
    x1, x2, x3 = x
    return np.array([
        x1**2 - 2*x1 + x2**2 - x3 + 1,
        x1*x2**2 - x1 - 3*x2 + x2*x3 + 2,
        x1*x3**2 - 3*x3 + x2*x3**2 + x1*x2
    ])

def J(x):
    x1, x2, x3 = x
    return np.array([
        [2*x1 - 2, 2*x2, -1],
        [x2**2 - 1, 2*x1*x2 - 3 + x3, x2],
        [x3**2 + x2, x3**2 + x1, 2*x1*x3 - 3 + 2*x2*x3]
    ])

x = np.array([1.,2.,3.])
r = np.array([1.,1.,1.])

errors = []

for k in range(7):
    print(k)
    e = np.linalg.norm(r - x)
    errors.append(e)
    s = np.linalg.solve(J(x), f(x))
    x = x - s
    print(errors)

for j in range(7):
    ratio = errors[j]/errors[j-1]
    print("Ratio:", ratio)

ratio = errors[6]/errors[5]
print("Final ratio:", ratio)
