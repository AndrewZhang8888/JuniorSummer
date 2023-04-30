import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import re
import sys

#In this analysis we start by reading in monthly LMP Data from the beginning of July 2021 up to the end of June 2022

'''
IF I COULD START OVER I WOULD MERGE THE DATAFRAMES THEN EDIT THAT WOULD BE EASIER
Here we read in the monthly CSVs of hourly day ahead lmp data from several listed regions
'''
lmp_1 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202107.csv')
lmp_2 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202108.csv')
lmp_3 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202109.csv')
lmp_4 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202110.csv')
lmp_5 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202111.csv')
lmp_6 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202112.csv')
lmp_7 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202201.csv')
lmp_8 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202202.csv')
lmp_9 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202203.csv')
lmp_10 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202204.csv')
lmp_11 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202205.csv')
lmp_12 = pd.read_csv(sys.path[0] + '\RTBM-LMP-MONTHLY-SL-202206.csv')

name_change_dict = {' PNODE Name':'PNODE Name', " Settlement Location Name":"Settlement Location Name", " Price Type":"Price Type", "HE01":" HE01"}


#Here we individually organize the monthly datasets of LMP into a daily database
lmp_1 = lmp_1.rename(columns = name_change_dict)
lmp_1 = lmp_1.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_1 = lmp_1[lmp_1['Price Type'] == 'LMP']
lmp_1 = lmp_1.reset_index()
lmp_1 = lmp_1.fillna(0)
lmp_1['Date'] = pd.to_datetime(lmp_1['Date'])
lmp_1['LMP'] = lmp_1.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_1 = lmp_1[keep_columns]
lmp_1 = lmp_1.groupby('Date').agg('mean')

lmp_2 = lmp_2.rename(columns = name_change_dict)
lmp_2 = lmp_2.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_2 = lmp_2[lmp_2['Price Type'] == 'LMP']
lmp_2 = lmp_2.reset_index()
lmp_2 = lmp_2.fillna(0)
lmp_2['Date'] = pd.to_datetime(lmp_2['Date'])
lmp_2['LMP'] = lmp_2.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_2 = lmp_2[keep_columns]
lmp_2 = lmp_2.groupby('Date').agg('mean')

lmp_3 = lmp_3.rename(columns = name_change_dict)
lmp_3 = lmp_3.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_3 = lmp_3[lmp_3['Price Type'] == 'LMP']
lmp_3 = lmp_3.reset_index()
lmp_3 = lmp_3.fillna(0)
lmp_3['Date'] = pd.to_datetime(lmp_3['Date'])
lmp_3['LMP'] = lmp_3.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_3 = lmp_3[keep_columns]
lmp_3 = lmp_3.groupby('Date').agg('mean')

lmp_4 = lmp_4.rename(columns = name_change_dict)
lmp_4 = lmp_4.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_4 = lmp_4[lmp_4['Price Type'] == 'LMP']
lmp_4 = lmp_4.reset_index()
lmp_4 = lmp_4.fillna(0)
lmp_4['Date'] = pd.to_datetime(lmp_4['Date'])
lmp_4['LMP'] = lmp_4.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_4 = lmp_4[keep_columns]
lmp_4 = lmp_4.groupby('Date').agg('mean')

lmp_5 = lmp_5.rename(columns = name_change_dict)
lmp_5 = lmp_5.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_5 = lmp_5[lmp_5['Price Type'] == 'LMP']
lmp_5 = lmp_5.reset_index()
lmp_5 = lmp_5.fillna(0)
lmp_5['Date'] = pd.to_datetime(lmp_5['Date'])
lmp_5['LMP'] = lmp_5.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_5 = lmp_5[keep_columns]
lmp_5 = lmp_5.groupby('Date').agg('mean')

lmp_6 = lmp_6.rename(columns = name_change_dict)
lmp_6 = lmp_6.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_6 = lmp_6[lmp_6['Price Type'] == 'LMP']
lmp_6 = lmp_6.reset_index()
lmp_6 = lmp_6.fillna(0)
lmp_6['Date'] = pd.to_datetime(lmp_6['Date'])
lmp_6['LMP'] = lmp_6.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_6 = lmp_6[keep_columns]
lmp_6 = lmp_6.groupby('Date').agg('mean')

lmp_7 = lmp_7.rename(columns = name_change_dict)
lmp_7 = lmp_7.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_7 = lmp_7[lmp_7['Price Type'] == 'LMP']
lmp_7 = lmp_7.reset_index()
lmp_7 = lmp_7.fillna(0)
lmp_7['Date'] = pd.to_datetime(lmp_7['Date'])
lmp_7['LMP'] = lmp_7.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_7 = lmp_7[keep_columns]
lmp_7 = lmp_7.groupby('Date').agg('mean')

lmp_8 = lmp_8.rename(columns = name_change_dict)
lmp_8 = lmp_8.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_8 = lmp_8[lmp_8['Price Type'] == 'LMP']
lmp_8 = lmp_8.reset_index()
lmp_8 = lmp_8.fillna(0)
lmp_8['Date'] = pd.to_datetime(lmp_8['Date'])
lmp_8['LMP'] = lmp_8.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_8 = lmp_8[keep_columns]
lmp_8 = lmp_8.groupby('Date').agg('mean')

lmp_9 = lmp_9.rename(columns = name_change_dict)
lmp_9 = lmp_9.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_9 = lmp_9[lmp_9['Price Type'] == 'LMP']
lmp_9 = lmp_9.reset_index()
lmp_9 = lmp_9.fillna(0)
lmp_9['Date'] = pd.to_datetime(lmp_9['Date'])
lmp_9['LMP'] = lmp_9.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_9 = lmp_9[keep_columns]
lmp_9 = lmp_9.groupby('Date').agg('mean')

lmp_10 = lmp_10.rename(columns = name_change_dict)
lmp_10 = lmp_10.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_10 = lmp_10[lmp_10['Price Type'] == 'LMP']
lmp_10 = lmp_10.reset_index()
lmp_10 = lmp_10.fillna(0)
lmp_10['Date'] = pd.to_datetime(lmp_10['Date'])
lmp_10['LMP'] = lmp_10.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_10 = lmp_10[keep_columns]
lmp_10 = lmp_10.groupby('Date').agg('mean')

lmp_11 = lmp_11.rename(columns = name_change_dict)
lmp_11 = lmp_11.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_11 = lmp_11[lmp_11['Price Type'] == 'LMP']
lmp_11 = lmp_11.reset_index()
lmp_11 = lmp_11.fillna(0)
lmp_11['Date'] = pd.to_datetime(lmp_11['Date'])
lmp_11['LMP'] = lmp_11.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_11 = lmp_11[keep_columns]
lmp_11 = lmp_11.groupby('Date').agg('mean')

lmp_12 = lmp_12.rename(columns = name_change_dict)
lmp_12 = lmp_12.set_index('PNODE Name').filter(regex = '^NPPD', axis = 0)
lmp_12 = lmp_12[lmp_12['Price Type'] == 'LMP']
lmp_12 = lmp_12.reset_index()
lmp_12 = lmp_12.fillna(0)
lmp_12['Date'] = pd.to_datetime(lmp_12['Date'])
lmp_12['LMP'] = lmp_12.iloc[:,4:28].mean(axis = 1)
keep_columns = ['PNODE Name','Date',"Settlement Location Name","Price Type","LMP"]
lmp_12 = lmp_12[keep_columns]
lmp_12 = lmp_12.groupby('Date').agg('mean')


#Now we can start merging these dataframes in chronological order based on the dates in each set
lmp = lmp_1.merge(lmp_2, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_3, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_4, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_5, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_6, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_7, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_8, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_9, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_10, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_11, on = ["Date","LMP"], how = "outer")
lmp = lmp.merge(lmp_12, on = ["Date","LMP"], how = "outer")
lmp = lmp.reset_index()
print(lmp)


'''
Now we need to graph a 2 week timescale in which the dates are listed in chronological order
'''

lmp['Date'] = pd.to_datetime(lmp['Date'])
lmp = lmp.sort_values(by=['Date'])
lmp = lmp.reset_index()
lmp = lmp.drop('index', axis=1)
lmp_2wks = lmp.groupby(pd.Grouper(freq = '2W', key = 'Date')).agg('mean').reset_index()
print(lmp_2wks)



'''
Now I will attempt to create a line graph of changes in LMP by day with the Minn.HUb power producing region.
'''
plt.style.use('seaborn')
lmp_chart = lmp_2wks.plot('Date','LMP', color = "k", linestyle = '--', linewidth = 3, marker = 'D', markerfacecolor = 'yellow', markeredgecolor = 'yellow')
ax = plt.gca()
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2.5)  # change width
    ax.spines[axis].set_color('#8B8989')    # change color
plt.xlabel('Date (Months)')
plt.ylabel('Day-Ahead LMP (Cents/KWH)')
plt.legend(prop={'size':20})
plt.tight_layout()
plt.show()
