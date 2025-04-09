import numpy as np
from scipy.optimize import minimize

def f(x):
    return x[0]**2 + 5*x[1]

initial_guess = [0, 0]
solution = minimize(f, initial_guess)
print(solution.x)
