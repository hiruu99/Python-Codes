'''
Answers for Lab 9 Question 4
Hiruni Anjana
29/1/2023
'''

from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
from scipy import stats

#Contingency table
df = pd.DataFrame([[1,10,37],[49,35,9]],index=['eaten','not_eaten'],columns=['uninfected','lightly_infected','highly_infected'])
print(df)

#Stacking the values in contingency table
df2 = df.stack()
print(df2)

#Converting to dictionary
df3 = df2.to_dict()
print(df3)

#Plot the mosaic plot
mosaic = mosaic(df3, gap=0.05)
plt.title("Mosaic plot")
plt.show()
plt.savefig("Mosaic.jpg")

#Chi-square contingency test
# t = stats.chi2_contingency(df)
# print("chi square statistic: ", t)
stats, p, dof, expected = chi2_contingency(df)
print("Chi-square statistic: ", stats)
print("p-value: ", p)
print("Degrees of freedom: ", dof)


expected_values_table = pd.DataFrame(chi.expected_freq, index=['eaten','not_eaten'], columns=['uninfected','lightly_infected','highly_infected'])
print(expected_values_table)
