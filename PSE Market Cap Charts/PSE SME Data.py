# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value presence of PSE listed small, medium 
# and emerging board companies. 


# Exercise Insights:
# The results show Injap Sia's MerryMart flourishing
# since its recent IPO

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
sme_coy = data_set.loc[267:274,"COMPANY NAME"]
sme_mc = data_set.loc[267:274,"MARKET CAPITALIZATION"]
fin_df = pd.DataFrame(data_set, index=[sme_coy, sme_mc])


plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.25, right=0.95)

plt.barh(y=sme_coy, width=sme_mc, color="brown")
plt.title("PSE Listed Companies \n Small, Medium and Emerging Board Sector", fontsize=13)
plt.xlabel("Market Cap Value in PHP", fontsize=10)
plt.xticks(fontsize=7)
plt.yticks(fontsize=8)

plt.show()