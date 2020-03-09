# Prabhas Kumra
# Assignment-5
# CS-458

import pandas as pd 

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

training_set = pd.read_csv('train.csv', header=0)
testing_set = pd.read_csv('test.csv', header=0)

# print(training_set)
# print(" ")
# print(testing_set)

df = pd.read_csv('mtcars.csv', header=0)

# training_set.drop('hp',implace=True)
# testing_set.drop('hp',implace=True)

# print(training_set)
# print(" ")
# print(testing_set)

del training_set['hp']
# training_set.drop('hp',  inplace=True)
del testing_set['hp']
# training_set.drop('hp', inplace=True)


# print(training_set)
# print(" ")
# print(testing_set)
# print(training_set)
# print(training_set.head())
X = training_set
Y = training_set.am

# print(X)
# print(Y)

# X_train, X_test, y_train, y_test = train_test_split(X,Y,train_size=0.3)

# print(X_test)

clf = LogisticRegression()
clf.fit(X,Y)
y_pred = clf.predict(testing_set)

print(y_pred)


# print("Accuracy: ", accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))

