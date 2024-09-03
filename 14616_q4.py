"""
Mock Exam
Hiruni Anjana
28/02/2023
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats

#Load the data
fish = pd.read_csv("ElectricFish.csv")

#Check data
print(fish.describe())

#Extract the data columns
difference = fish["Difference"]

#Draw the histogram
fig, axs = plt.subplots(figsize=(8, 4))
sns.histplot(difference, bins=30, kde=True, ax=axs)
plt.title("Histogram of number of species difference between upstream and downstream")
plt.xlabel("Number of species difference")
#plt.show()
plt.savefig("Histogram_q4.jpg", dpi=100)

#Shapiro test
stat, p = stats.shapiro(difference)
print("For difference: stat=%.3f, p value=%.3f" % (stat, p))

#Paired sample t-test
stat1, p1 = stats.ttest_rel(fish["speciesUpstream"], fish["speciesDownstream"])
print("Test statistic: ", stat1)
print("p-value: ", p1)





