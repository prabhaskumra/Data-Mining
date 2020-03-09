# Prabhas Kumra
# Assignment-5
# CS-458

import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv('mtcars.csv', header=0)

del df['hp']
del df['car_model']

X = df

Y = df.am
# del X['am']
# print (Y)



X_train, X_test, y_train, y_test = train_test_split(X,Y,train_size=0.25)


print(X_train)
print(y_train)

clf = LogisticRegression()
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

print(y_pred)


print("Accuracy: ", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

