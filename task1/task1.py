import matplotlib.pyplot as plt
import numpy as np


labels = ['arctan(x)', 'Analytical second derivative', 'Calculated second derivative', 'Difference of results']

h = 10 ** -3
x = np.linspace(-np.pi / 2, np.pi / 2, 100)

func = lambda xi: np.arctan(xi)

#Calculating second deriative, using calculate analitical function
analitDer = lambda xi: -2 * x / (1 + x ** 2) ** 2

#Calculating second deriative, using calculate function for calculating
calcDer = lambda xi: (np.arctan(x) - 2 * np.arctan(x - h) + np.arctan(x - 2 * h)) / h ** 2

fig, ax = plt.subplots(4, figsize=(12, 7))


def main():
    #Ploting function, second deriatives and difference of results
    ax[0].plot(x, func(x), color='black', label=labels[0])
    ax[1].plot(x, analitDer(x), color='red', label=labels[1])
    ax[2].plot(x, calcDer(x), color='green', label=labels[2])
    ax[3].plot(x, analitDer(x) - calcDer(x), color='blue', label=labels[3])

    for i in range(len(labels)):
        if i == 0 or i == 3:
            ax[i].legend(loc='lower right')
        else:
            ax[i].legend(loc='upper right')
        ax[i].grid()

    fig.suptitle('Сomparison of the second derivative of arctan(x) calculated by calculation and analytically',
                 fontsize=16)
    plt.show()


if __name__ == '__main__':
    main()
