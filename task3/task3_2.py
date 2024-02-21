#Task 2
# Importing libraries
import matplotlib.pyplot as plt
import numpy as np


# Accuracy and interval
e = 10 ** (-4)
x = np.linspace(-3, 3, 500)


# Function
def function(x_):
    return 2 ** x_ - 5 * x_ - 3


# The derivative of function
def function_derivative(x_):
    return 2 ** x_ * np.log(2) - 5


# Newton 's Method
def newtons_method(a: float, b: float, func, func_der) -> (float, int):
    iterations_count = 0
    x0 = (a + b) / 2
    x1 = x0 - func(x0) / func_der(x0)
    while abs(x1 - x0).all() >= e:
        x0 = x1
        x1 = x0 - func(x0) / func_der(x0)
        iterations_count += 1

    return x1, iterations_count


# The method of simple iterations
def simple_iterations_method(func, func_der) -> (float, int):
    iterations_count = 0
    x0 = -1
    while abs(func(x0)) >= e:
        x1 = x0 - func(x0) / func_der(x0)
        x0 = x1
        iterations_count += 1
    return x0, iterations_count


# Plotting result
fig, ax = plt.subplots(2, figsize=(12, 7))
fig.suptitle('Function considering on the interval [-3, 3]')

ax[0].plot(x, function(x))
ax[0].set_title("Newton's method")
ax[0].plot(newtons_method(-3, 3, function, function_derivative)[0],
           function(newtons_method(-3, 3, function, function_derivative)[0]),
           color='red', marker='o',
           label=f'Root: {newtons_method(-3, 3, function, function_derivative)[0]}'
                 f'\nCount of iterations: {newtons_method(-3, 3, function, function_derivative)[1]}')
ax[0].legend(loc='upper right')
ax[0].grid()

ax[1].plot(x, function(x), color='green')
ax[1].set_title("The method of simple iterations")
ax[1].plot(simple_iterations_method(function, function_derivative)[0],
           function(simple_iterations_method(function, function_derivative)[0]), color='purple',
           marker='o', label=f'Root: {simple_iterations_method(function, function_derivative)[0]}\n'
           f'Count of iterations: {simple_iterations_method(function, function_derivative)[1]}')
ax[1].legend(loc='upper right')
ax[1].grid()

plt.show()
