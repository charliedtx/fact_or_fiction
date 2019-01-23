import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from numpy import nan


# In[54]:


lebanon = pd.read_csv('./data/clean_data/population-lebanon.csv')

#source = http://www.worldometers.info/world-population/lebanon-population/


# In[50]:


refugees_lebanon = pd.read_csv('./data/clean_data/syr-reg_ref_by_date-lebanon.csv')

#source = https://data2.unhcr.org/en/situations/syria/location/71

refugees_lebanon['first of year'][1] = refugees_lebanon['individuals'][1]


# In[55]:


refugees_lebanon = refugees_lebanon.dropna()


# In[56]:


lebanon = lebanon.dropna()


# In[57]:


refugees_lebanon =refugees_lebanon.reset_index()


# In[58]:


refugees_lebanon['Date'] = 0


# In[59]:


for i in range(len(refugees_lebanon)):

    refugees_lebanon['Date'][i] = float(refugees_lebanon['data_date'][i][-4:])


# In[60]:


refugees_lebanon = refugees_lebanon.rename(columns={'Date': 'Year'})


# In[61]:


lebanon = lebanon.reset_index()


# In[62]:


type(lebanon['Year'][0])


# In[63]:


lebanon = lebanon.merge(refugees_lebanon, on='Year')


# In[64]:


lebanon


# In[65]:


#plt.bar(turkey['Year'], turkey['Population']/1000000)


#plt.bar(round(lebanon['Year']), (lebanon['individuals']/100)/(lebanon['Population']/10000))
#plt.xticks([2015, 2016, 2017, 2018])

#plt.ylabel('Refugees as a percent of total Population')

#This is probably the best chart to show a crisis. The bottom chart is a bit underwhelming.


# In[68]:


#plt.bar(lebanon['Year'], lebanon['Population']/1000000)
#plt.xticks([2015, 2016, 2017, 2018])
#plt.bar(lebanon['Year'], lebanon['individuals']/1000000, label="Refugees")
#plt.ylabel('Lebanon population in millions')
#plt.legend()




jordan = pd.read_csv('./data/clean_data/population-jordan.csv', thousands=',')

#source = http://www.worldometers.info/world-population/jordan-population/


# In[3]:


refugees_jordan = pd.read_csv('./data/clean_data/syr-reg_ref_by_date-lebanon.csv', thousands=',')

#source = https://data2.unhcr.org/en/situations/syria/location/36

refugees_jordan['first of year'][1] = refugees_jordan['individuals'][1]


# In[4]:


refugees_jordan = refugees_jordan.dropna()


# In[5]:


jordan = jordan.dropna()


# In[6]:


refugees_jordan =refugees_jordan.reset_index()


# In[7]:


refugees_jordan['Date'] = 0


# In[8]:


for i in range(len(refugees_jordan)):

    refugees_jordan['Date'][i] = float(refugees_jordan['data_date'][i][-4:])


# In[9]:


refugees_jordan = refugees_jordan.rename(columns={'Date': 'Year'})


# In[10]:


jordan = jordan.reset_index()


# In[11]:


type(jordan['Year'][0])


# In[12]:


jordan = jordan.merge(refugees_jordan, on='Year')


# In[13]:


jordan


# In[14]:


#plt.bar(turkey['Year'], turkey['Population']/1000000)


#plt.bar(round(jordan['Year']), (jordan['individuals']/100)/(jordan['Population']/10000))
#plt.xticks([2015, 2016, 2017, 2018])

#plt.ylabel('Refugees as a percent of total Population')

#This is probably the best chart to show a crisis. The bottom chart is a bit underwhelming.


# In[15]:


#plt.bar(jordan['Year'], jordan['Population']/1000000)
#plt.xticks([2015, 2016, 2017, 2018])
#plt.bar(jordan['Year'], jordan['individuals']/1000000, label="Refugees")
#plt.ylabel('Jordan population in millions')
#plt.legend()


turkey = pd.read_csv('./data/clean_data/population-turkey.csv', thousands=",")

#source = http://www.worldometers.info/world-population/turkey-population/


# In[3]:


refugees_turkey = pd.read_csv('./data/clean_data/syr-reg_ref_by_date-turkey.csv')

#source = https://data2.unhcr.org/en/situations/syria/location/113

refugees_turkey['first of year'][1] = refugees_turkey['individuals'][1]


# In[4]:


refugees_turkey = refugees_turkey.dropna()


# In[5]:


turkey = turkey.dropna()


# In[6]:


refugees_turkey =refugees_turkey.reset_index()


# In[9]:


refugees_turkey['Date'] = 0


# In[10]:


for i in range(len(refugees_turkey)):

    refugees_turkey['Date'][i] = float(refugees_turkey['data_date'][i][-4:])


# In[11]:


refugees_turkey = refugees_turkey.rename(columns={'Date': 'Year'})


# In[12]:


turkey = turkey.reset_index()


# In[13]:


type(turkey['Year'][0])


# In[18]:


turkey = turkey.merge(refugees_turkey, on='Year')


# In[30]:


turkey


# In[31]:


#plt.bar(turkey['Year'], turkey['Population']/1000000)


plt.bar(round(lebanon['Year']), (lebanon['individuals']/100)/(lebanon['Population']/10000), label='Lebanon', width=.1)
plt.bar(round(jordan['Year'])+.1, (jordan['individuals']/100)/(jordan['Population']/10000), label='Jordan', width=.1)
plt.bar(round(turkey['Year'])+.2, (turkey['individuals']/100)/(turkey['Population']/10000), label='Turkey', width=.1)
plt.xticks([2015, 2016, 2017, 2018])

plt.ylabel('Refugees as a percent of total Population')
plt.legend()


plt.show()


#This is probably the best chart to show a crisis. The bottom chart is a bit underwhelming.


# In[44]:


#plt.bar(turkey['Year'], turkey['Population']/1000000)
#plt.xticks([2015, 2016, 2017, 2018])
#plt.bar(turkey['Year'], turkey['individuals']/1000000, label="Refugees")
#plt.ylabel('Turkey population in millions')
#plt.legend()


