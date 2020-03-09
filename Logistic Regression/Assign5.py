# Prabhas Kumra
# Assignment-5
# CS-458

import pandas as pd 
import copy

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

training_set = pd.read_csv('train.csv', header=0)
testing_set = pd.read_csv('test.csv', header=0)


del training_set['hp']
del testing_set['hp']

X = training_set
Y = training_set.am
del X['car_model']
del testing_set['car_model']

y_true = copy.deepcopy(testing_set.am)


clf = LogisticRegression(max_iter=1000)
clf.fit(X,Y)
y_pred = clf.predict(testing_set)

print("Accuracy: ", accuracy_score(y_true, y_pred))
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))

