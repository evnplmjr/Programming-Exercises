# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value of the PSE's only ETF in the market


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
etf_coy = data_set.loc[0,"COMPANY NAME"]
etf_mc = data_set.loc[0,"MARKET CAPITALIZATION"]
etf_df = pd.DataFrame(data_set, index=[etf_coy, etf_mc])


plt.figure(figsize=[20, 30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.29, right=0.95, top=0.80, bottom=0.16)

plt.barh(y=etf_coy, width=etf_mc, color="skyblue", align="center")
plt.title("PSE Listed Companies \n ETF Sector \n", fontsize=15)

plt.text(0.8, 0.1, """    The First Metro Exchange Traded Fund \n 
    is the only exchange traded fund in the \n
    Philippine Stock Exchange. It is managed by \n
    First Metro Asset Management.""")

plt.xlabel("Market Cap Value in PHP", fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=10)

plt.show()
