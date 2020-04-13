# Prabhas Kumra
# CS458
# Assignment 8

import numpy as np

data = np.genfromtxt("data.txt", delimiter=",")

k = int(data[0][0])
m = int(data[0][1])

data = np.delete(data,0,0)
