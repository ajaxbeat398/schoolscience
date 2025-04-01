import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Example function: f(x) = x^2 - 4x + 3
    return x ** 2 - 4 * x + 3

a = -1.0
b = 5.0
n = 1000
h = (b - a) / n

# Generate points between a and b
x = np.linspace(a, b, n)
y = f(x)

plt.plot(x, y)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function f(x) = x^2 - 4x + 3')

# Add legend
plt.legend(['f(x)', 'y-axis'])

# Show plot
plt.show()
