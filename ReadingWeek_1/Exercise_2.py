# Problem: Evaluate 0.4 - 0.3 with Python or Matlab with up to 17 significant digits

# First partproblem: What do you observe? Explain what happened.

def Evaluate(a, b):
    return a-b

print(Evaluate(0.4, 0.3))

# Output: 0.10000000000000003

def makeFloatToAnyBase(number, base, precision=17):
    newNumberConversion = "0."
    frac = number
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for _ in range(precision):
        frac *= base
        digit = int(frac)
        newNumberConversion += digits[digit]
        frac -= digit

        if frac == 0:
            break

    return newNumberConversion

a = makeFloatToAnyBase(0.4, 2)
b = makeFloatToAnyBase(0.3, 2)
print(a, b)

c = makeFloatToAnyBase(0.1, 2)

print(c)

import math as math
def f(x):
    return math.cos(x) - math.sin(x)

def bisection_method(f, a, b, tolerance = 10^-6, k=20):
    for _ in range(k):
        mid = (a + b)/2
        fc = f(mid)
        if abs(fc) < tolerance or (b - a )/ 2 < tolerance:
            return mid # solution found
        
        if f(a) * fc < 0:
            b = mid
        else:
            a = mid

    return (a+b)/2

a, b = 0, 1

root = bisection_method(f, a, b)
print("Root: ", root)

print("Cosinus with our root", math.cos(root))
print("Sinus with our root", math.sin(root))

