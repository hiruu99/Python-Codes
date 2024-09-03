'''
Answers for Lab 10 Question 1
Hiruni Anjana
01/02/2023
'''

#Import the packages
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

#Read the iris data file into a Pandas DataFrame
dataframe = pd.read_csv("iris.csv")

#Extract the sepal length and sepal width
sepal_data = dataframe.loc[:, 'sepal.length':'sepal.width']

#Pick the best K value for the algorithm
k_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wcss_error = []
for k in k_values:
    model = KMeans(n_clusters=k)
    model.fit(sepal_data)
    wcss_error.append(model.inertia_)
print(wcss_error)

plt.xlabel("Number of clusters")
plt.ylabel("wcss_error")
plt.plot(k_values,wcss_error)
plt.show()

#Preprocessing
pre_s = StandardScaler().fit(sepal_data)
#Standardized data
standard_data_s = pre_s.transform(sepal_data)

#print(kmeans.cluster_centers_)
kmeans_s = KMeans(n_clusters=3).fit(sepal_data)
centroid_s = kmeans_s.cluster_centers_
print("Sepal length and width values for the centroids: ", centroid_s)
labels_s = kmeans_s.labels_

#Create a 2D array
P_sepal = np.array([[4.6, 3.0], [6.2, 3.0]])

#Predict the species
pred_s = kmeans_s.predict(P_sepal)
print("Predicted labels for sepal data: ", pred_s)

#Scatter plot for the sepal measurement data
plt.scatter(sepal_data.iloc[:, 0], sepal_data.iloc[:, 1], c=labels_s.astype(float), s=50, cmap='summer')
plt.scatter(centroid_s[:, 0], centroid_s[:, 1], c='red', s=100, alpha=0.9)
plt.scatter(P_sepal[:,0], P_sepal[:, 1], c='black', s=100)

#Label data points
for i, txt in enumerate(labels_s):
    plt.annotate(txt, (sepal_data['sepal.length'][i], sepal_data['sepal.width'][i]))
plt.scatter(P_sepal[:, 0], P_sepal[:, 1], c="black", s=50)

#print labels to new data values
for i, txt in enumerate(pred_s):
    plt.annotate(txt, (P_sepal[:, 0][i], P_sepal[:, 1][i]))

#Label each data point with its species name
for i, label in enumerate(dataframe['v_short']):
    plt.annotate(label, (sepal_data.iloc[i]['sepal.length'], sepal_data.iloc[i]['sepal.width']), xytext=(-20, 20),fontsize=6,
                 color="brown",ha='center', va='center',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color="orange"),  textcoords="offset points")

plt.title("Sepal measurement data")
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.savefig("Sepal_scatter.jpg")
plt.show()


#Petal data
petal_data = dataframe.loc[:, 'petal.length':'petal.width']

#Preprocessing
pre_p = preprocessing.StandardScaler().fit(petal_data)
standard_data_p = pre_p.transform(petal_data)

#print(kmeans.cluster_centers_)
kmeans_p = KMeans(n_clusters=3).fit(petal_data)
centroid_p = kmeans_p.cluster_centers_
labels_p = kmeans_p.labels_

#Create a 2D array
P_petal = np.array([[1.5, 0.2], [4.1, 1.2]])

pred_p = kmeans_p.predict(P_petal)
print("Predicted labels for petal data: ", pred_p)

#Scatter plot for the petal measurement data
plt.scatter(petal_data.iloc[:, 0], petal_data.iloc[:, 1], c=labels_s.astype(float), s=50, cmap='summer')
plt.scatter(centroid_p[:, 0], centroid_p[:, 1], c='red', s=50, alpha=0.9)
plt.scatter(P_petal[:, 0], P_petal[:, 1], c='black', s=100)

#Label data points
for i,txt in enumerate(labels_p):
    plt.annotate(txt,(petal_data['petal.length'][i],petal_data['petal.width'][i]))
plt.scatter(P_petal[:,0],P_petal[:,1],c="black",s=50)

#print labels to new data values
for i, txt in enumerate(pred_p):
    plt.annotate(txt, (P_petal[:, 0][i], P_petal[:, 1][i]))

#Label each data point with its species name
for i, label in enumerate(dataframe['v_short']):
    plt.annotate(label, (petal_data.iloc[i]['petal.length'], petal_data.iloc[i]['petal.width']), xytext=(-20, 20), fontsize=6,
                 ha='center', va='center',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color="orange"), color="brown", textcoords="offset points")

plt.title("Petal measurement data")
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()
plt.savefig("Petal_scatter.jpg")
plt.show()



