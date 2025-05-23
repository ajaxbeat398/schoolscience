import numpy as np
import matplotlib.pyplot as plt

def draw_linear_curve():
    x = np.linspace(0, 10, 100)
    y = x * np.sin(x) + np.cos(x)
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    draw_linear_curve()
