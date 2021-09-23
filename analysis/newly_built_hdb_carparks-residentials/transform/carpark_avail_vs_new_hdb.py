import pandas as pd
import numpy as np

# select data year:
year = 2019

hdb = pd.read_csv(f'D:\ARP\VISUALISATION\output\hdb_resident_carpark_newbuild\hdb-resident-or-carpark-{year}.csv') # take processed data (mewly built hdb residentials or carparks)
cp = pd.read_csv('D:\ARP\VISUALISATION\source\hdb-property-information\(hai)carpark-by-district.csv') # carpark by districts data
cpavail = pd.read_csv('D:\ARP\VISUALISATION\TEST\\2020-01-01=00+00+00.csv') ## any transformed carpark avail data

hdb.residential = pd.Series(np.where(hdb.residential.values == 'Y', 1, 0), ##convert Y, N value to binary
          hdb.index)

hdb.multistorey_carpark = pd.Series(np.where(hdb.multistorey_carpark.values == 'Y', 1, 0),
          hdb.index)

hdb = hdb.groupby('bldg_contract_town', as_index=False).sum() # grpby and count number of residential building and number of carpark
df = pd.merge(cpavail,cp,on='number') # merge carpark by district to carpark availability matched on carpark name

df = df.groupby('region', as_index=False).sum() # grpby region and calculate sum of
df =  pd.merge(df,hdb,left_on='region', right_on='bldg_contract_town') #merge df and hdb matched on region
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] ### drop unnamed columns
df.drop(columns=['year_completed'], inplace=True)  ##drop year completed and unnamed columns
print(df)

df.to_csv(f'carpark_avail_vs_new_hdb-{year}.csv')