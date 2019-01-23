import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from numpy import nan

#Here we import the data. Gabby did this using a nice function, which I duplicated here.

dhs = {'table13':pd.read_excel("./data/clean_data/fy2016_table13.xls", header=3, skipfooter=2, na_values=['-','D'])}
def get_data_by_table_number(table_number):
    return dhs.get(f'table{table_number}')

lebanon = pd.read_csv('./clean_data/population-lebanon.csv')

#source = http://www.worldometers.info/world-population/lebanon-population/

refugees_lebanon = pd.read_csv('./data/clean_data/syr-reg_ref_by_date-lebanon.csv')

#source = https://data2.unhcr.org/en/situations/syria/location/71

refugees_lebanon['first of year'][1] = refugees_lebanon['individuals'][1]

refugees_lebanon = refugees_lebanon.dropna()

lebanon = lebanon.dropna()

refugees_lebanon =refugees_lebanon.reset_index()

refugees_lebanon['Date'] = 0

for i in range(len(refugees_lebanon)):

    refugees_lebanon['Date'][i] = float(refugees_lebanon['data_date'][i][-4:])

refugees_lebanon = refugees_lebanon.rename(columns={'Date': 'Year'})

lebanon = lebanon.reset_index()

type(lebanon['Year'][0])

lebanon = lebanon.merge(refugees_lebanon, on='Year')

lebanon
#plt.bar(turkey['Year'], turkey['Population']/1000000)


#plt.bar(round(lebanon['Year']), (lebanon['individuals']/100)/(lebanon['Population']/10000))
#plt.xticks([2015, 2016, 2017, 2018])

#plt.ylabel('Refugees as a percent of total Population')

#This is probably the best chart to show a crisis. The bottom chart is a bit underwhelming.
#plt.bar(lebanon['Year'], lebanon['Population']/1000000)
#plt.xticks([2015, 2016, 2017, 2018])
#plt.bar(lebanon['Year'], lebanon['individuals']/1000000, label="Refugees")
#plt.ylabel('Lebanon population in millions')
#plt.legend()

jordan = pd.read_csv('./data/clean_data/population-jordan.csv', thousands=',')

#source = http://www.worldometers.info/world-population/jordan-population/
refugees_jordan = pd.read_csv('./data/raw_data/syr-reg_ref_by_date-jordan.csv', thousands=',')

#source = https://data2.unhcr.org/en/situations/syria/location/36

refugees_jordan['first of year'][1] = refugees_jordan['individuals'][1]
refugees_jordan = refugees_jordan.dropna()

jordan = jordan.dropna()

refugees_jordan =refugees_jordan.reset_index()

refugees_jordan['Date'] = 0

for i in range(len(refugees_jordan)):

    refugees_jordan['Date'][i] = float(refugees_jordan['data_date'][i][-4:])

refugees_jordan = refugees_jordan.rename(columns={'Date': 'Year'})

jordan = jordan.reset_index()

type(jordan['Year'][0])

jordan = jordan.merge(refugees_jordan, on='Year')

jordan
####
#This is all duplicates of the above code. Making a relatively simple bar chart for the proportion by population.


turkey = pd.read_csv('./Turkey Population .csv', thousands=",")

#source = http://www.worldometers.info/world-population/turkey-population/
refugees_turkey = pd.read_csv('./data/clean_data/syr-reg_ref_by_date-turkey.csv')

#source = https://data2.unhcr.org/en/situations/syria/location/113

refugees_turkey['first of year'][1] = refugees_turkey['individuals'][1]
refugees_turkey = refugees_turkey.dropna()

turkey = turkey.dropna()

refugees_turkey =refugees_turkey.reset_index()

refugees_turkey['Date'] = 0

for i in range(len(refugees_turkey)):

    refugees_turkey['Date'][i] = float(refugees_turkey['data_date'][i][-4:])

refugees_turkey = refugees_turkey.rename(columns={'Date': 'Year'})

turkey = turkey.reset_index()

type(turkey['Year'][0])

turkey = turkey.merge(refugees_turkey, on='Year')

turkey

#plt.bar(turkey['Year'], turkey['Population']/1000000)


refugees = get_data_by_table_number('table13')
refugees = pd.read_excel("./data/fy2016_table13.xls", header=3, skipfooter=2, na_values=['-','D'])
usa = pd.read_excel("./usa_population.xlsx")
usa2 = pd.read_excel('./usa_refugees2.xlsx')

#This data is from the Refugee Processing Center http://www.wrapsnet.org/archives/
#It provides monthly data through September 2018.

usa2['cumulative'] = usa2['refugees'].cumsum()

x = int(usa2['cumulative'][20]) - int(usa2['cumulative'][11])

new = {'Year': 2017,
                'Number': usa2['cumulative'][11]
                }
new2 = {'Year': 2018,
                'Number': x
                }

refugees = refugees.append(new, ignore_index=True)

refugees = refugees.append(new2, ignore_index=True)

refugees['Arrivals since 1980 (No deaths)'] = refugees['Number'].cumsum()


#This is incorporating the current USA death rate of 8.33 per 1000 population per year.

refugees['Estimated refugee population'] = 0

refugees['Estimated refugee population'][0] = (1-(8.33/1000))*refugees['Arrivals since 1980 (No deaths)'][0]

for i in range(1,len(refugees)):
    refugees['Estimated refugee population'][i] = ((1-(8.33/1000))*refugees['Number'][i])+ refugees['Estimated refugee population'][i-1] 



#Here we graph everything out. You can see on the x-values of the below graphs that there is offsetting so the bars will be adjascent. 

newdf = refugees[refugees['Year']>2014]
usa2 = usa[['Year', 'Population']]
usa2 = usa2.dropna()
newdf = newdf.merge(usa2, on='Year')


plt.bar(round(newdf['Year'])+.3, (newdf['Estimated refugee population']/100)/(newdf['Population']/10000), label='USA', width=.1)



plt.bar(round(lebanon['Year']), (lebanon['individuals']/100)/(lebanon['Population']/10000), label='Lebanon', width=.1)
plt.bar(round(jordan['Year'])+.1, (jordan['individuals']/100)/(jordan['Population']/10000), label='Jordan', width=.1)
plt.bar(round(turkey['Year'])+.2, (turkey['individuals']/100)/(turkey['Population']/10000), label='Turkey', width=.1)
plt.xticks([2015, 2016, 2017, 2018])

plt.ylabel('Refugees as a percent of total Population')
plt.legend()

plt.show()

#Thank you! Easter egg goes here: "patrolling the Mojave almost makes you wish for a nuclear winter..." 
