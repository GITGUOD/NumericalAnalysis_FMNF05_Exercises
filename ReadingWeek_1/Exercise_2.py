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
    """
    Solve f(x) = 0 using the bisection method.
    
    Arguments:
    f -- function
    a, b -- interval [a, b]
    tol -- tolerance
    max_iter -- maximum iterations
    
    Returns:
    x_root -- approximate root
    """
    for _ in range(k):
        mid = (a + b)/2
        fc = f(mid) # new mid
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

import math

def fixed_point_iteration(g, g_prime, x0, tol=1e-8, max_iter=1000):
    """
    Performs fixed-point iteration to solve x = g(x)
    
    Parameters:
    g        : function, the fixed-point function
    g_prime  : function, derivative of g
    x0       : float, initial guess
    tol      : float, tolerance for convergence
    max_iter : int, maximum number of iterations
    
    Returns:
    x_star   : float, approximate fixed point
    """
    # Check convergence condition |g'(x0)| < 1
    if abs(g_prime(x0)) >= 1:
        print("Warning: Initial value may not lead to convergence (|g'(x0)| >= 1).")
        return None

    x_old = x0
    for k in range(max_iter):
        x_new = g(x_old)
        
        # Check for convergence
        if abs(x_new - x_old) < tol:
            print(f"Converged in {k+1} iterations.")
            return round(x_new, 8)  # 8 decimal digits
        
        x_old = x_new

    print("Did not converge within the maximum number of iterations.")
    return None

# Example usage with the functions from your exercise 5:

# Function f(x) = 1/2*x + 1/x
def f(x):
    return 0.5*x + 1/x
def f_prime(x):
    return 0.5 - 1/(x**2)

# Function g(x) = 2/3*x + 2/(3*x)
def g_func(x):
    return 2/3*x + 2/(3*x)
def g_prime_func(x):
    return 2/3 - 2/(3*x**2)

# Function h(x) = 3/4*x + 1/(2*x)
def h(x):
    return 0.75*x + 1/(2*x)
def h_prime(x):
    return 0.75 - 1/(2*x**2)

# User's initial guess
x0 = 1.0

# Solve each equation
solution_f = fixed_point_iteration(f, f_prime, x0)
solution_g = fixed_point_iteration(g_func, g_prime_func, x0)
solution_h = fixed_point_iteration(h, h_prime, x0)

print("Solution for f(x):", solution_f)
print("Solution for g(x):", solution_g)
print("Solution for h(x):", solution_h)


# (a) x^3 = 2x + 2
g_a = lambda x: (2*x + 2)**(1/3)
g_a_prime = lambda x: (2/3)*(2*x + 2)**(-2/3)

# (b) e^x + x = 7
g_b = lambda x: 7 - math.exp(x)
g_b_prime = lambda x: -math.exp(x)

# (c) e^x + sin(x) = 4
g_c = lambda x: math.log(4 - math.sin(x))
g_c_prime = lambda x: -math.cos(x)/(4 - math.sin(x))

# Initial guesses
x0_a = 1.5
x0_b = 1.0
x0_c = 1.0

sol_a, iter_a = fixed_point_iteration(g_a, g_a_prime, x0_a)
sol_b, iter_b = fixed_point_iteration(g_b, g_b_prime, x0_b)
sol_c, iter_c = fixed_point_iteration(g_c, g_c_prime, x0_c)

print(f"(a) x = {sol_a:.8f} in {iter_a} iterations")
print(f"(b) x = {sol_b:.8f} in {iter_b} iterations")
print(f"(c) x = {sol_c:.8f} in {iter_c} iterations")

print("Test")

print("Test")
print("Test")

print("Test")
print("Test")
print("Test")
print("Test")