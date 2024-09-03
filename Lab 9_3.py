'''
Answers for Lab 9 Question 3
Hiruni Anjana
29/1/2023
'''

import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.gofplots import qqplot
import scipy.stats as stats
import seaborn as sns

#Load the csv file
Birds = pd.read_csv("BlackbirdTestosterone.csv")
Birds = Birds.dropna()
#print(Birds[['log before','log after', 'dif in logs']].describe())

#Statistics for log before
log_before = Birds["log before"]
print(log_before.describe())

#Statistics for log after
log_after = Birds["log after"]
print(log_after.describe())

#Statistics for log difference
dif = Birds["dif in logs"]
print(dif.describe())

#Plot the histograms for each sample
sns.histplot(Birds, kde=True, x=Birds["dif in logs"])
plt.title("Histogram of log difference")
#plt.show()
plt.savefig("Histogram_log.jpg")

#Plot the Quantile-Quantile plot
qqplot(Birds["dif in logs"], xlabel="dif in logs", line='s')
plt.title("QQplot of log difference")
plt.show()
plt.savefig("QQplot_log.jpg")

#shapiro test
stat, p = stats.shapiro(dif)
print("stat=%.3f p value=%.3f" % (stat, p))

#boxplot
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].boxplot(Birds["Before"])
axs[0].set_title("Boxplot of before sample")

axs[1].boxplot(Birds["After"])
axs[1].set_title("Boxplot of after sample")
plt.show()
plt.savefig("Boxplot.jpg")

#Violin plot
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].violinplot(Birds["Before"])
axs[0].set_title("Violin plot of before sample")

axs[1].violinplot(Birds["After"])
axs[1].set_title("Violin plot of after sample")
plt.show()
plt.savefig("Violinplot.jpg")

#Paired sample t test
stats, p = stats.ttest_rel(Birds["Before"], Birds["After"])
print("stat=%.3f p value=%.3f" % (stats, p))
