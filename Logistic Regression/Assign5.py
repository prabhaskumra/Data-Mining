# Prabhas Kumra
# Assignment-5
# CS-458

import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

training_set = pd.read_csv('train.csv', header=0)
testing_set = pd.read_csv('test.csv', header=0)

del training_set['hp']
del testing_set['hp']

X = training_set[['mpg','cyl','disp','drat','wt','qsec','vs','gear','carb']]
Y = training_set.am

testing = testing_set[['mpg','cyl','disp','drat','wt','qsec','vs','gear','carb']]
y_true = testing_set.am

clf = LogisticRegression(solver="lbfgs", max_iter=1000)
clf.fit(X,Y)
y_pred = clf.predict(testing)

print("Accuracy: ", accuracy_score(y_true, y_pred))
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))

