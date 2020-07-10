# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value presence of PSE listed companies
# in the industrial sector


# Exercise Insights:
# The results show that San Miguel, Manila Electric and 
# Universal Robina are the top three companies that are
# above and beyond the industrial sector's average market cap
# value


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
industrial_coy = data_set.loc[72:140,"COMPANY NAME"]
industrial_mc = data_set.loc[72:140,"MARKET CAPITALIZATION"]
ind_df = pd.DataFrame(data_set, index=[industrial_coy, industrial_mc])


plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.18, right=0.95, top=0.96, bottom=0.06)

plt.barh(y=industrial_coy, width=industrial_mc, color="red")
plt.title("PSE Listed Companies in the Industrial Sector", fontsize=10)
plt.xlabel("Market Cap Value in PHP", fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=6)

plt.show()