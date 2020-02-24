# Prabhas Kumra
# CS-458
# Assignment-1

import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(10)
y = np.zeros(10)

i = 0
with open("myData.txt", "r") as filestream:
    for line in filestream:
        currentLine = line.split(",")
        x[i] = int(currentLine[0])
        y[i] = int(currentLine[1])
        i+=1

xySum = 0
xSqSum = 0
ySqSum = 0
xSum = 0
ySum = 0

for z in range(0,np.size(x)):
    xySum += x[z]*y[z]
    xSqSum += x[z]*x[z]
    ySqSum += y[z]*y[z]
    xSum += x[z]
    ySum += y[z]
    
slope = ( (np.size(x) * xySum) - (xSum*ySum)) / ( (np.size(x)*xSqSum) - (xSum*xSum) )

intercept = (ySum - (slope*xSum))/np.size(x)

plt.axis([1000, 2500, 150000, 450000])
t = np.linspace(1000,2500, 20)

plt.plot(x,y,'ro', t, slope*t + intercept, 'b-', t, slope*t + intercept, 'y-')
plt.show()




















