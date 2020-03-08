# Prabhas Kumra
# Assignment-5
# CS-458

import pandas as pd 

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

training_set = pd.read_csv('train.csv')
testing_set = pd.read_csv('test.csv')

# print(training_set)
# print(" ")
# print(testing_set)


# training_set.drop('hp',implace=True)
# testing_set.drop('hp',implace=True)
del training_set['hp']
del testing_set['hp']

# print(training_set)
# print(" ")
# print(testing_set)




