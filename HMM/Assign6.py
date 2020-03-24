# Prabhas Kumra
# Assignment #6
# CS-458

import numpy as np
from hmmlearn import hmm
# np.reandom.seed(42)

transmat = np.array([[0.304, 0.696],
                     [0.831, 0.169]])

emitmat = np.array([[0.533, 0.065, 0.402],
                    [0.342, 0.334, 0.324]])

startprob = np.array([0.5, 0.5])

h = hmm.MultinomialHMM(n_components=2)
h.startprob_ = startprob
h.transmat_ = transmat
h.emissionprob_ = emitmat

# works fine
# h.fit([[0, 0, 1, 0, 0]]) 

# print (h.decode([0, 0, 1, 0, 0]))
# print (h)
X = np.atleast_2d([1, 3, 2, 2, 3, 3, 2, 3, 2, 2]).T
print(h.decode(X))
