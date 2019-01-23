import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib


jordan = pd.read_excel('./data/raw_data/regfugees-jordan.xlsx')
turkey = pd.read_excel('./data/raw_data/refugees-turkey.xlsx')
lebanon = pd.read_excel('./data/raw_data/refugees-lebanon.xlsx')

yval = np.arange(0,3590000)

plt.rcParams['font.size'] = 15
plt.figure(figsize=(16,10))
plt.grid(axis='y')
plt.plot(jordan['date'], jordan['refugees']/1000000, label="Jordan")
plt.plot(turkey['date'], turkey['refugees']/1000000, label='Turkey')
plt.plot(lebanon['date'], lebanon['refugees']/1000000, label='Lebanon')
plt.legend()

plt.ylabel('Total Refugees in Millions', fontsize=18)

usa = pd.read_excel('./usa_refugees.xlsx')

plt.rcParams['font.size'] = 15
plt.figure(figsize=(16,10))
plt.grid(axis='y')
plt.plot(jordan['date'], jordan['refugees']/1000000, label="Jordan")
plt.plot(turkey['date'], turkey['refugees']/1000000, label='Turkey')
plt.plot(lebanon['date'], lebanon['refugees']/1000000, label='Lebanon')
plt.plot(usa['date'], usa['refugees']/1000000, label='USA')
plt.legend()

plt.ylabel('Total Refugees in Millions', fontsize=18)
plt.show()
