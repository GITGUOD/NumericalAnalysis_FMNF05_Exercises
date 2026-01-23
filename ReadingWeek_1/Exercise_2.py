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

print(0.01100110011001100 - 0.01001100110011001)