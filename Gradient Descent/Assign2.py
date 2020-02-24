# Prabhas Kumra
# Assignment-2
# CS-458

import numpy as np 
import matplotlib.pyplot as plt 


# funtion reads a list of numbers and normalize each item in the list
def min_max(list):
    newList = [0] * list.size
    minList, maxList = min(list), max(list)
    for x, item in enumerate(list):
        newList[x] = (item-minList)/ (maxList-minList)
    return newList

# computes the total error for a given value of m and b
def square_error(m, b, data):
    x, y = data.T
    yNot = m * x + b 
    error = 0
    for i in range(0, y.size):
       error +=  (y[i]-yNot[i])**2
    return error

# computes the gradients based on the partial derivates 
# and updates m and b with learing rate alpha and derivatives 
def gradient(b, m, data, alpha):
    x, y = data.T
    xNorm = min_max(x)
    yNorm = min_max(y)
    yNot = 0
    derivateB = 0
    derivateM = 0

    for i in range(0, y.size):
        yNot = m * xNorm[i] + b 
        derivateB += (-1*(yNorm[i] - yNot))  
        derivateM += (-1*(yNorm[i] - yNot)) * xNorm[i]

    m = m - alpha * derivateM
    b = b - alpha * derivateB

    return m, b

# main function
def model():
    data = np.genfromtxt("myData.txt", delimiter=",")
    m = np.random.rand()
    b = np.random.rand()
    alpha = 0.01
    iteration = 1000
    squaredError = square_error(m,b,data)
    x, y = data.T

    # Run Gradient Descent
    for i in range(0, iteration):
        m, b = gradient(b, m, data, alpha)

    # Plot the regression line
    t = np.linspace(100,25, 250)
    plt.plot(x,y,'ro', t, m*t + b, 'b-', t, m*t + b, 'y-')
    plt.show()

if __name__ == "__main__":
    model()




