# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value presence of PSE listed financial 
# companies. 

# Exercise Insights:
# The results showed the dominance of foreign insurance 
# companies, and the top Filipino banks trailing at almost half of
# the leading market cap value. 

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
financials_coy = data_set.loc[1:30,"COMPANY NAME"]
financials_mc = data_set.loc[1:30,"MARKET CAPITALIZATION"]
fin_df = pd.DataFrame(data_set, index=[financials_coy, financials_mc])


plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.25, right=0.95)

plt.barh(y=financials_coy, width=financials_mc, color="green")
plt.title("PSE Listed Companies \n Financial Sector", fontsize=13)
plt.xlabel("Market Cap Value in PHP", fontsize=10)
plt.xticks(fontsize=7)
plt.yticks(fontsize=8)

plt.show()
    
