'''
Answers for Lab 9 Question 1
Hiruni Anjana
29/1/2023
'''

from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.gofplots import qqplot
import seaborn as sns

#Load the csv file
temperature = pd.read_csv("Temperature.csv")

#Print the mean, SD, count, minimum and maximum
print(temperature.describe())

#Plot the histogram
sns.histplot(temperature, x="temperature", kde=True)
plt.title("Histogram of temperature")
plt.show()
plt.savefig("Histogram_temp.jpg")

#Plot the Quantile-Quantile plot
qqplot(temperature, line='s')
plt.title("QQplot pf temperature")
plt.show()
plt.savefig("QQplot_temp.jpg")

#Shapiro test
stat, p = stats.shapiro(temperature)
print("stat=%.3f p value=%.3f" % (stat, p))

#Google-scipy one sample t test
test, p = stats.ttest_1samp(temperature, popmean=98.6, alternative="two-sided" )
print('Test statistics:', test)
print('p value:', p)