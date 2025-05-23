import matplotlib.pyplot as plt
import numpy as np

x_values = [1, 2, 3, 4, 5]
y_values = [i * i for i in x_values]

plt.plot(x_values, y_values)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of X vs Y values')
plt.show()
