# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value presence of PSE listed property 
# companies. 

# Exercise Insights:
# The  data shows that SM and Ayala own much of the
# market cap value of the property sector. This is no
# surprise given the abundance of malls and condominiums
# developed by these property giants


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
prprty_coy = data_set.loc[165:202,"COMPANY NAME"]
prprty_mc = data_set.loc[165:202,"MARKET CAPITALIZATION"]
fin_df = pd.DataFrame(data_set, index=[prprty_coy, prprty_mc])


plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.25, right=0.95)

plt.barh(y=prprty_coy, width=prprty_mc, color="orange")
plt.title("PSE Listed Companies \n Property Sector", fontsize=13)
plt.xlabel("Market Cap Value in PHP", fontsize=10)
plt.xticks(fontsize=7)
plt.yticks(fontsize=8)

plt.show()
    