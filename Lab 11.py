'''
Answers for lab 11
07/02/2023
'''

#Import the packages
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

#Load the Iris dataset
iris = pd.read_csv("iris.csv")

#Split the measurement data and class labels (species) to X and Y variables
X = iris.iloc[:, 0:4]
Y = iris.iloc[:, 5]

#Output the species category values of the Y variable
category = (iris["v_short"].unique())
print("Species category values of the Y variable: ", category)

#Replace the category values with integer numbers
label = preprocessing.LabelEncoder()
x = label.fit(category)
Y = label.transform(Y)

#Output updated Y values
print("Category values with integer numbers: ", Y)

#Split the Iris dataset (X and Y variables) to train and test data
X_train, X_test,Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

#Training
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)

#Standardization
X_train_standard = scaler.transform(X_train)
X_test_standard = scaler.transform(X_test)

#MLPClassifier=Artificial Neural Network
from sklearn.neural_network import MLPClassifier

#Create a neural network with multiple layers
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)

#Fit this into the dataset
mlp.fit(X_train_standard, Y_train.ravel())

#Predict the species labels for the test data
pred_y = mlp.predict(X_test_standard)

from sklearn.metrics import classification_report, confusion_matrix

#Print classification report and confusion matrix
print("Confusion matrix: ")
print(confusion_matrix(Y_test, pred_y))
print("Classification report: ")
print(classification_report(Y_test, pred_y))

Plant = np.array([[5.9, 3.0, 7.0, 5.0], [4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]])
print(Plant)

scaler = StandardScaler()
scaler.fit(Plant)

#Standardization
Plant_standard = scaler.transform(Plant)

#Prediction
pred_p = mlp.predict(Plant_standard)

print("Predicted labels: ",pred_p)

#Change the number of neurons in each hidden layer to 2
mlp = MLPClassifier(hidden_layer_sizes=(2, 2, 2), max_iter=1000)

#Fit this into the dataset
mlp.fit(X_train_standard, Y_train.ravel())

#Use the trained model for predicting the species labels of the test data
pred_y = mlp.predict(X_test_standard)

from sklearn.metrics import classification_report, confusion_matrix

print("Confusion matrix: ")
print(confusion_matrix(Y_test, pred_y))
print("Classification report: ")
print(classification_report(Y_test, pred_y))






