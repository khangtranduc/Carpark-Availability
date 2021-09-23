import pandas as pd
import os, glob

for year in range(2018,2022):

    dir = f'D:/ARP/data_{year}/transform/merged/{year}_merged_all.csv' ## take output file from merge_all.py
    output = f'{dir}/../calsummonth/'

    if not os.path.isdir(output):
        os.mkdir(output)

    df = pd.read_csv(dir)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')] ### drop unnamed columns
    df.drop(columns=['avail_percent'], inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['period'] = df['date'].dt.to_period('M')
    df = df.groupby(df['period'], as_index=False).sum()
    df['avail_percent'] = round((df['available']/df['total']), 3) ## round up to 3dp
    df = df.reset_index(drop=True)
    df.to_csv(f'{output}{year}_trans_s_pm_a.csv', index = False) ## transformed - sum - per month - all