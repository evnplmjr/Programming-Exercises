# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value presence of PSE listed mining and oil
# companies. 

# Exercise Insights:
# The results highlight the dominance of the Semirara
# Mining Corp in the mining and oil sector, and Nickel Asia 
# and Atok-Big WEedge following suit with just half the 
# total market cap value of that of Semirara


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
miningoil_coy = data_set.loc[141:164,"COMPANY NAME"]
miningoil_mc = data_set.loc[141:164,"MARKET CAPITALIZATION"]
fin_df = pd.DataFrame(data_set, index=[miningoil_coy, miningoil_mc])


plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.25, right=0.95)

plt.barh(y=miningoil_coy, width=miningoil_mc, color="yellow")
plt.title("PSE Listed Companies \n Mining and Oil Sector", fontsize=13)
plt.xlabel("Market Cap Value in PHP", fontsize=10)
plt.xticks(fontsize=7)
plt.yticks(fontsize=8)

plt.show()