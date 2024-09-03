'''
Answers for Lab 10 Question 2
Hiruni Anjana
01/02/2023
'''

import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

#Load the iris data
irdata = iris.data

#Extract the labels
labels = iris.target

#Preprocessing
scaler = StandardScaler().fit(irdata)
#Standardized data
std_irdata = scaler.transform(irdata)

#Create a test data record
testdata = [[4.6, 3.0, 1.5, 0.2]]

#Standardization
std_testdata = scaler.transform(testdata)

#Create a 2-d array for the two data records (Plant 1 and Plant 2)
p = np.array([[4.6, 3.0, 1.5, 0.2], [6.2, 3.0,4.1,1.2]])

#Standardize the array
scaler_p = StandardScaler().fit(p)
std_testdata_p = scaler_p.transform(p)

#Train the KNN model using only the sepal measurements
sepaldata = std_irdata[:, [0, 1]]

#Find the two nearest neighbors of the test data record
testsepal = std_testdata[:, [0, 1]]

#Two nearest neighbhors
nn_1 = KNeighborsClassifier(n_neighbors=2)
nn_1.fit(sepaldata, labels)

# Predict the two nearest neighbors
indices = nn_1.kneighbors(testsepal, return_distance=False)
neighbors = iris.data[indices]
neighbors_labels = iris.target[indices]
neighbors_species = [iris.target_names[i] for i in neighbors_labels]

# Print the indices, data values, labels, and species of the two-nearest neighbors
print("Indices of the two-nearest neighbors:", indices)
print("Data values of the two-nearest neighbors:", neighbors)
print("Labels of the two-nearest neighbors:", neighbors_labels)
print("Species of the two-nearest neighbors:", neighbors_species)

#Five nearest neighbhors
nn_2 = KNeighborsClassifier(n_neighbors=5)
nn_2.fit(sepaldata, labels)

#Predict the probability of each plant categorizing into each species
sepal_probs = nn_2.predict_proba(testsepal[:,[0,1]])
print("Sepal Probabilities: ", sepal_probs)

# Predict the class labels for the two plants
sepal_labels = nn_2.predict(testsepal[:,[0,1]])
print("Sepal Labels:", sepal_labels)
print("Species predicted from the KNN algorithm: ", iris.target_names[sepal_labels[0]])


#Train the KNN model using only the petal measurements
petaldata = std_irdata[:, [2, 3]]

#Find the two nearest neighbors of the test data record
testpetal = std_testdata[:, [2, 3]]

#Two nearest neighbhors
nn_2 = KNeighborsClassifier(n_neighbors=2)
nn_2.fit(petaldata, labels)

# Predict the two nearest neighbors
indices_2 = nn_2.kneighbors(testpetal, return_distance=False)
neighbors_2 = iris.data[indices_2]
neighbors_labels_2 = iris.target[indices_2]
neighbors_species_2 = [iris.target_names[i] for i in neighbors_labels_2]

# Print the indices, data values, labels, and species of the two-nearest neighbors
print("Indices of the two-nearest neighbors:", indices_2)
print("Data values of the two-nearest neighbors:", neighbors_2)
print("Labels of the two-nearest neighbors:", neighbors_labels_2)
print("Species of the two-nearest neighbors:", neighbors_species_2)

#Five nearest neighbhors
nn_2 = KNeighborsClassifier(n_neighbors=5)
nn_2.fit(petaldata, labels)

#Predict the probability of each plant categorizing into each species
petal_probs = nn_2.predict_proba(testpetal[:,[0,1]])
print("Petal Probabilities: ", petal_probs)

# Predict the class labels for the two plants
petal_labels = nn_2.predict(testpetal[:,[0,1]])
print("Petal Labels:", petal_labels)
print("Species predicted from the KNN algorithm: ", iris.target_names[petal_labels[0]])


#Train the KNN model using both the sepal and petal measurements
alldata = std_irdata[:, [0, 1, 2, 3]]

#Find the two nearest neighbors of the test data record
testall = std_testdata[:, [0, 1, 2, 3]]

nn_3 = KNeighborsClassifier(n_neighbors=2)
nn_3.fit(alldata, labels)

# Predict the two nearest neighbors
indices_3 = nn_3.kneighbors(testall, return_distance=False)
neighbors_3 = iris.data[indices_3]
neighbors_labels_3 = iris.target[indices_3]
neighbors_species_3 = [iris.target_names[i] for i in neighbors_labels_3]

# Print the indices, data values, labels, and species of the two-nearest neighbors
print("Indices of the two-nearest neighbors:", indices_3)
print("Data values of the two-nearest neighbors:", neighbors_3)
print("Labels of the two-nearest neighbors:", neighbors_labels_3)
print("Species of the two-nearest neighbors:", neighbors_species_3)

#Five nearest neighbhors
nn_3 = KNeighborsClassifier(n_neighbors=5)
nn_3.fit(alldata, labels)

#Predict the probability of each plant categorizing into each species
all_probs = nn_3.predict_proba(testall[:1])
print("Probability: ", all_probs)

# Predict the class labels for the two plants
all_labels = nn_3.predict(testall[:1])
print("Labels:", all_labels)
print("Species predicted from the KNN algorithm: ", iris.target_names[all_labels[0]])


