import pandas as pd
import os, glob

dir = f'D:/ARP/VISUALISATION/Testcode/test_source/year'
output = f'{dir}/month'

if not os.path.isdir(output):
    os.mkdir(output)

all_files = glob.glob(dir + "/*.csv")
print(all_files)
for f in all_files:
    df = pd.read_csv(f)
    df.drop(columns=['avail_percent', 'Unnamed: 0'], inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['period'] = df['date'].dt.to_period('M')
    df = df.groupby(df['period'], as_index=False).sum()
    df['avail_percent'] = round((df['available']/df['total']), 3) ## round up to 3dp
    df.reset_index(drop=True, inplace=True)
    df.to_csv(f'{output}/{f}trans_s_pm_a.csv', index = False) ## transformed - sum - per month - all