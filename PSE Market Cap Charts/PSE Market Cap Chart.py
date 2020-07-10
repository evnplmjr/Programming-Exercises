from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import csv

data_set = pd.read_csv("PSE DATA.csv")



financials_coy = data_set.loc[1:30,"COMPANY NAME"]
financials_mc = data_set.loc[1:30,"MARKET CAPITALIZATION"]
fin_list = []
for fin_a, fin_b in zip(financials_coy, financials_mc):
    fin_list.append([fin_a, fin_b])
fin_df = pd.DataFrame(data=fin_list)
fin_mc_total = fin_df[1].sum()
print("Total Market Cap Value - Financials")
print(fin_mc_total)


holdingfirms_coy = data_set.loc[31:71,"COMPANY NAME"]
holdingfirms_mc = data_set.loc[31:71,"MARKET CAPITALIZATION"]
hf_list = []
for hf_a, hf_b in zip(holdingfirms_coy, holdingfirms_mc):
    hf_list.append([hf_a, hf_b])
hf_df = pd.DataFrame(data=hf_list)
hf_mc_total = hf_df[1].sum()
print("Total Market Cap Value - Holding Firms")
print(hf_mc_total)


industrial_coy = data_set.loc[72:140,"COMPANY NAME"]
industrial_mc = data_set.loc[72:140,"MARKET CAPITALIZATION"]
ind_list = []
for ind_a, ind_b in zip(industrial_coy, industrial_mc):
    ind_list.append([ind_a, ind_b])
ind_df = pd.DataFrame(data=ind_list)
ind_mc_total = ind_df[1].sum()
print("Total Market Cap Value - Industrial")
print(ind_mc_total)


miningoil_coy = data_set.loc[141:164,"COMPANY NAME"]
miningoil_mc = data_set.loc[141:164,"MARKET CAPITALIZATION"]
mo_list = []
for mo_a, mo_b in zip(miningoil_coy, miningoil_mc):
    mo_list.append([mo_a, mo_b])
mo_df = pd.DataFrame(data=mo_list)
mo_mc_total = mo_df[1].sum()
print("Total Market Cap Value - Mining and Oil")
print(mo_mc_total)


prprty_coy = data_set.loc[165:202,"COMPANY NAME"]
prprty_mc = data_set.loc[165:202,"MARKET CAPITALIZATION"]
pty_list = []
for pty_a, pty_b in zip(prprty_coy, prprty_mc):
    pty_list.append([pty_a, pty_b])
pty_df = pd.DataFrame(data=pty_list)
pty_mc_total = pty_df[1].sum()
print("Total Market Cap Value - Property")
print(pty_mc_total)


services_coy = data_set.loc[203:266,"COMPANY NAME"]
services_mc = data_set.loc[203:266,"MARKET CAPITALIZATION"]
ser_list = []
for ser_a, ser_b in zip(services_coy, services_mc):
    ser_list.append([ser_a, ser_b])
ser_df = pd.DataFrame(data=ser_list)
ser_mc_total = ser_df[1].sum()
print("Total Market Cap Value - Services")
print(ser_mc_total)


sme_coy = data_set.loc[267:274,"COMPANY NAME"]
sme_mc = data_set.loc[267:274,"MARKET CAPITALIZATION"]
sme_list = []
for sme_a, sme_b in zip(sme_coy, sme_mc):
    sme_list.append([sme_a, sme_b])
sme_df = pd.DataFrame(data=sme_list)
sme_mc_total = sme_df[1].sum()
print("Total Market Cap Value - Small, Medium and Emerging")
print(sme_mc_total)

etf_mc_total = data_set.loc[0,"MARKET CAPITALIZATION"]
print("Total Market Cap Value - Exchange Traded Funds")
print(etf_mc_total)

mc_total = (fin_mc_total + hf_mc_total + ind_mc_total 
            + mo_mc_total + pty_mc_total + ser_mc_total 
            + sme_mc_total + etf_mc_total)
print("Overall Market Cap Value as of Q2 2020")
print(mc_total)



plt.figure(figsize=[20,30])
plt.style.use("seaborn")
plt.gca()
plt.subplots_adjust(left=0.15, right=0.95, top=0.85, bottom=0.15)

x_total = ["Financial", "Holding Firms", "Industrial", "Mining and Oil", "Property", "Services", "SME", "ETF"]
y_total = [fin_mc_total, hf_mc_total, ind_mc_total, mo_mc_total, pty_mc_total, ser_mc_total, sme_mc_total, etf_mc_total]

main_chart = plt.bar(x=x_total , height=y_total)

main_chart[0].set_color("green")
main_chart[1].set_color("blue")
main_chart[2].set_color("red")
main_chart[3].set_color("yellow")
main_chart[4].set_color("orange")
main_chart[5].set_color("purple")
main_chart[6].set_color("brown")
main_chart[7].set_color("skyblue")

plt.title("Philippine Stock Exchange \n Market Cap Value per Sector \n Q2 2020", fontsize=14)
plt.xlabel("Sector", fontsize=11)
plt.xticks(fontsize=8)
plt.ylabel("Market Cap Value in PHP \n Ranging from 1.5B to 3.5T", fontsize=11)
plt.yticks(fontsize=8)

plt.show()