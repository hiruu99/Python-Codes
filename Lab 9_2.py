'''
Answers for Lab 9 Question 2
Hiruni Anjana
29/1/2023
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import scipy.stats as stats

#Load the csv file
lizards = pd.read_csv("HornedLizards.csv")
lizards = lizards.dropna()

#Filter the horn lengths of living lizards
survived = lizards[lizards["Survive"] == "survived"]
#Print the statistics of the horn lengths of living lizards
print(survived.describe())

#Filter the horn lengths of dead lizards
dead = lizards[lizards["Survive"] == "dead"]
#Print the statistics of the horn lengths of dead lizards
print(dead.describe())

#Plot the histograms for each sample
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(survived, bins=30, kde=True, ax=axs[0])
axs[0].set_title("Histogram of living lizards")
sns.histplot(dead, bins=30, kde=True, ax=axs[1])
axs[1].set_title("Histogram of dead lizards")
plt.show()
plt.savefig("Histogram_lizards.jpg")

#Plot the Quantile-Quantile plot
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
sm.qqplot(survived["Squamosal horn length"], line="s", ax=axs[0])
axs[0].set_title("QQplot of living lizards")
sm.qqplot(dead["Squamosal horn length"], line="s", ax=axs[1])
axs[1].set_title("QQplot of dead lizards")
plt.show()
plt.savefig("QQplot_lizards.jpg")

#Shapiro test
stat_survived, p_survived = stats.shapiro(survived["Squamosal horn length"])
print("stat=%.3f p value=%.3f" % (stat_survived, p_survived))

stat_dead, p_dead = stats.shapiro(dead["Squamosal horn length"])
print("stat=%.3f p value=%.3f" % (stat_dead, p_dead))

#boxplot
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].boxplot(survived["Squamosal horn length"])
axs[0].set_title("Boxplot of living lizards")

axs[1].boxplot(dead["Squamosal horn length"])
axs[1].set_title("Boxplot of dead lizards")
plt.show()
plt.savefig("Boxplot_lizards.jpg")

#Violin plot
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].violinplot(survived["Squamosal horn length"])
axs[0].set_title("Violin plot of living lizards")

axs[1].violinplot(dead["Squamosal horn length"])
axs[1].set_title("Violin plot of dead lizards")
plt.show()
plt.savefig("Violinplot_lizards.jpg")

#Mann-whitney test
stats, p = stats.mannwhitneyu(survived["Squamosal horn length"], dead["Squamosal horn length"], alternative="two-sided")
print("stat=%.3f p value=%.3f" % (stats, p))


