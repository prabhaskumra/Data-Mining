# Prabhas Kumra
# Assignment-5
# CS-458

import pandas as pd 

training_set = pd.read_csv('train.csv')
testing_set = pd.read_csv('test.csv')

print(training_set)
print(" ")
print(testing_set)


del training_set['hp']
del testing_set['hp']

print(training_set)
print(" ")
print(testing_set)


