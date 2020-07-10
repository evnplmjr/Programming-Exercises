# Exercise Objective: 
# Produce a data visualization output to determine the
# market cap value presence of PSE listed companies in
# the services sector

# Exercise Insights:
# The results show a diverse mix of key players in 
# the services sector. Telecoms like Globe and PLDT, 
# port operations like ICTSI, and memorial park
# developer, Golden Bria.
 

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv


data_set = pd.read_csv("PSE DATA.csv", index_col=False)
services_coy = data_set.loc[203:266,"COMPANY NAME"]
services_mc = data_set.loc[203:266,"MARKET CAPITALIZATION"]
fin_df = pd.DataFrame(data_set, index=[services_coy, services_mc])


plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.25, right=0.95, top=0.95, bottom=0.07)

plt.barh(y=services_coy, width=services_mc, color="purple")
plt.title("PSE Listed Companies in the Services Sector", fontsize=10)
plt.xlabel("Market Cap Value in PHP", fontsize=8)
plt.xticks(fontsize=6)
plt.yticks(fontsize=7)

plt.show()
    
