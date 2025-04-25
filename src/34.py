import numpy as np
from scipy import optimize

def f(x):
    return x**2 - 5*x + 6

result = optimize.fsolve(f, 3)
print("The solution is:", result)
