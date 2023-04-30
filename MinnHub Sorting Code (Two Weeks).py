import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import re
import sys

'''
Here we read in the CSV of hourly day ahead lmp data from several listed regions
'''
lmp = pd.read_csv(sys.path[0] + "\(Past 365 days) MISO Day-Ahead Energy Price.csv")
#print(lmp['node'].unique())
lmp = lmp[lmp['node']=='MINN.HUB']
lmp.index = np.arange(0, len(lmp))
#new_lmp = lmp.copy(deep=True)
for a in range(len(lmp['Date'])):
    old_date = lmp.iloc[a]['Date']
    #print(old_date)
    new_date = re.split('\s',old_date)[0]
    #print(new_date)
    lmp.iloc[a,0] = new_date


'''
Here we work with the newly aggregated data of LMP means averaged per day. This data is only for stations within the Minn.HUB power distribution area.
'''
lmp_mean = lmp.groupby('Date').agg('mean')
lmp_mean = lmp_mean.reset_index()
lmp_mean['Date'] = pd.to_datetime(lmp_mean['Date'])
lmp_mean = lmp_mean.sort_values(by=['Date'])
lmp_mean = lmp_mean.reset_index()
lmp_mean = lmp_mean.drop('index', axis=1)
lmp_mean = lmp_mean.groupby(pd.Grouper(freq = '2W', key = 'Date')).agg('mean').reset_index()
print(lmp_mean)

'''
Now I will attempt to create a line graph of changes in LMP by day with the Minn.HUb power producing region.
'''
plt.style.use('seaborn')
lmp_chart = lmp_mean.plot('Date','lmp', color = "k", linestyle = '--', linewidth = 3, marker = 'D', markerfacecolor = 'yellow', markeredgecolor = 'yellow')
ax = plt.gca()
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2.5)  # change width
    ax.spines[axis].set_color('#8B8989')    # change color
plt.xlabel('Date (Months)')
plt.ylabel('Day-Ahead LMP (Cents/KWH)')
plt.legend(prop={'size':20})
plt.tight_layout()



plt.show()