import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def polynomial_function(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


np.random.seed(0)
x_values = np.linspace(-10, 10, 30)
true_params = [-1, 2, 1.5, 2]
y_values = polynomial_function(x_values, *true_params) + np.random.normal(0.0, 50, len(x_values))

parameters, parameters_covariance = curve_fit(polynomial_function, x_values, y_values)

plt.scatter(x_values, y_values, label="Points")
plt.plot(x_values, polynomial_function(x_values, *parameters))
plt.legend()
plt.show()
