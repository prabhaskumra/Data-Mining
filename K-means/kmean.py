# Prabhas Kumra
# CS458
# Assignment 8

import numpy as np

data = np.genfromtxt("data.txt", delimiter=",")

k = int(data[0][0])

m = int(data[0][1])

hell = {1.37, 1.1
        1.3, 0.2
        0.6, 2.8 
        3.0, 3.2 
        1.2, 0.7 
        1.4, 1.6 
        1.2, 1.0 
        1.2, 1.1 
        0.6, 1.5 
        1.8, 2.6 
        1.2, 1.3 
        1.2, 1.0 
        0.0, 1.9}

data = np.delete(data,0,0)

