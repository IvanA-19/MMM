# Task1
# Importing libraries
import matplotlib.pyplot as plt
import numpy as np


# Accuracy and interval
e = 10 ** (-4)
x = np.linspace(-1, 1, 500)


# Function
def function(x0: np.ndarray) -> float:
    return 3 * (x0 ** 4) + 8 * (x0 ** 3) + 6 * (x0 ** 2) - 10


# The dichotomy method
def dichotomy_method(a: float, b: float, func) -> (float, int):
    iterations_count = 0
    c = (a + b) / 2
    while(abs(func(c))) >= e:
        c = (a + b) / 2
        if(func(a) * func(c)) < 0:
            a = a
            b = c
        else:
            a = c
            b = b
        iterations_count += 1

    return (a + b) / 2, iterations_count


# The chord method
def chord_method(curr: float, prev: float, func) -> (float, int):
    iterations_count = 0
    nxt = 0
    while abs(curr - prev) > e:
        temp = nxt
        nxt = prev - (func(prev) * (curr - prev))/(func(curr) - func(prev))
        prev = curr
        curr = temp
        iterations_count += 1
    return nxt, iterations_count


# Plotting result
fig, ax = plt.subplots(2, figsize=(12, 7))
fig.suptitle('Function considering on the interval [-1, 1]')

ax[0].plot(x, function(x))
ax[0].set_title('The dichotomy method')
ax[0].plot(dichotomy_method(-1, 1, function)[0], function(dichotomy_method(-1, 1, function)[0]), color='red',
           marker='o', label=f'Root: {dichotomy_method(-1, 1, function)[0]}\n'
           f'Count of iterations: {dichotomy_method(-1, 1, function)[1]}')
ax[0].legend(loc='upper left')
ax[0].grid()

ax[1].plot(x, function(x), color='green')
ax[1].set_title('The chord method')
ax[1].plot(chord_method(-1, 1, function)[0], function(chord_method(-1, 1, function)[0]), color='purple',
           marker='o', label=f'Root: {chord_method(-1, 1, function)[0]}\n'
           f'Count of iterations: {chord_method(-1, 1, function)[1]}')
ax[1].legend(loc='upper left')
ax[1].grid()

plt.show()
