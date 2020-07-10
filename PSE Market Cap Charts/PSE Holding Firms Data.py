# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value presence of PSE listed holding firms


# Exercise Insights:
# The results show that SM leads the pack, with the Ayalas, 
# Gokongweis and San Miguel trailing at only half of SM's market cap


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
holdingfirms_coy = data_set.loc[31:71,"COMPANY NAME"]
holdingfirms_mc = data_set.loc[31:71,"MARKET CAPITALIZATION"]
hf_df = pd.DataFrame(data_set, index=[holdingfirms_coy, holdingfirms_mc])


plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.18, right=0.95)

plt.barh(y=holdingfirms_coy, width=holdingfirms_mc, color="blue")
plt.title("PSE Listed Companies \n Holding Firms Sector", fontsize=13)
plt.xlabel("Market Cap Value in PHP", fontsize=10)
plt.xticks(fontsize=7)
plt.yticks(fontsize=8)

plt.show()