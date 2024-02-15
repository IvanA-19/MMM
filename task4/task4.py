import numpy as np
import matplotlib.pyplot as plt
from csv import reader


# reading csv
file = "03_Санкт-Петербург (1).csv"


data = []
with open(file, "r") as rfile:
    for row in reader(rfile):
        data.append(row)
    data.pop(0)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])


for row in data:
    print(row)


# Lagrange polynomial
def getLagrangePolynomial(x_val, y_val):
    basePolynomial = []
    for i in range(len(x_val)):
        n = 1
        for j in range(len(x_val)):
            if j != i:
                n *= ((x-x_val[j])/(x_val[i]-x_val[j]))
        basePolynomial.append(n)

    def LagrangePolynomial():
        result = 0
        for e in range(len(y_val)):
            result += y_val[e] * basePolynomial[e]
        return result
    return LagrangePolynomial


t = 3
year = 13
xValues = []
yValues = []
count = -1

while len(xValues) != 12:
    if data[year][t] < 999.9:
        xValues.append(data[year][0])
        yValues.append(data[year][t])
        count += 1
    year += 1
x = np.arange(xValues[0], xValues[count] + 0.1, 0.1)


polynomial = getLagrangePolynomial(xValues, yValues)
plt.plot(x, polynomial())
plt.plot(xValues, yValues, 'ro')
plt.suptitle("Lagrange polynomial")
plt.grid()
plt.show()
