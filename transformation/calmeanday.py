import pandas as pd
from datetime import datetime
import os

ti1 = datetime.now()
print(ti1)

dir = 'D:/ARP/data_2018/temp/'
output = f'{dir}/../transform/'
if not os.path.isdir(output):
    os.mkdir(output)

df = None

for f_name in os.listdir(dir):
    df_tmp = pd.read_csv(dir+f_name)
    # DRop unamed column and 0 lots value
    df_tmp = df_tmp.loc[:, ~df_tmp.columns.str.contains('^Unnamed')]
    df_tmp = df_tmp.loc[~(df_tmp['total'] == 0)]
    date=df_tmp.time.str.split(' ').str.get(0).unique()[0]
    print (date)
    df_tmp = df_tmp.groupby(['number'], as_index=False).mean().astype({'total': 'int16', 'available': 'int16'}).sort_values('total', ascending=True)
    # print(df_tmp.dtypes)
    df_tmp['avail_percent'] = round((df_tmp['available']/df_tmp['total']), 3)
    # drop row with available > total and carpark with > 4443 lots
    df_tmp = df_tmp.loc[~(df_tmp['avail_percent'] > 1) & ~(df_tmp['total'] > 4443)]
    # add a column of date
    df_tmp['date'] = date
    # reset and drop index
    df_tmp.reset_index(drop=True, inplace=True)
    #df = df_tmp if df is None else pd.concat([df,df_tmp]) #this is for extracting data from multiples files and concatenating them
    df_tmp.to_csv(f'{output+date}-trans_m_pd_pc.csv', index = False) 
    
##### FILE NAMING CONVENTION:
# trans: transformed
# m: mean
# pd: per day
# pc: per carpark

# df.groupby(['number']).mean().sort_values('total', ascending=True)
# df['avail_percent'] = df['available'] / df['total'] # add a column of exact number of feature 


#df_out = df[['ID','avail_percent']].drop_duplicates()

# df.to_csv('00test_out.csv', index = False)
print ('----------------------- Total runtime:  %s ------------------' % (datetime.now() - ti1))
