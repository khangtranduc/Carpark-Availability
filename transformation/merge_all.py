#### USE THIS TO MERGE TO calmeanday.py output to a file
import glob, os
import pandas as pd
year = 2021

dir = f'D:/ARP/data_{year}/transform/'
output = f'{dir}/merged/'
if not os.path.isdir(output):
    os.mkdir(output)

all_files = glob.glob(dir + "/*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files))
df = df.reset_index(drop=True)
df.to_csv(f'{output}{year}_merged_all.csv', index = False)