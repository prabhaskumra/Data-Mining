# Prabhas Kumra
# Assignment #6
# CS-458

import numpy as np

print("States:  A     B")
print("-----------------------")
print("Symbols: x  y  z")

states = {'x':0, 'y':1, 'z':2}
# review_dictionary = {'text':review_text, 'sentiment': category}
x = [0, 2, 1, 1, 2, 2, 1, 2, 1, 1]

# Initial Probabilities
pi = np.array([0.5, 0.5])
print("-----------------------")
print("Initial Probabilities:")
print(pi)

# Transition Probabilities
A = np.array([[0.303, 0.697],[0.831, 0.169]])
print("-----------------------")
print("Transition Probabilites:")
print(A)

# Emmision Probabilities
B = np.array([[0.533, 0.065, 0.402],[0.342, 0.334, 0.324]])
print("-----------------------")
print("Emission Probabilites:")
print(B)
print("-----------------------")
# Using forward algorithm
M = len(x)
N = pi.shape[0]

alpha = np.zeros((M, N))
alpha[0, :] = pi * B[:,x[0]]

for t in range(1, M):
    for j in range(N):
        for i in range(N):
            alpha[t, j] += alpha[t-1, i] * A[i, j] * B[j, x[t]]

prob = np.sum(alpha[M-1,:])

print("Probability of the sequence is: ", prob)
