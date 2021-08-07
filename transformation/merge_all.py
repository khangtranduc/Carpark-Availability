#### USE THIS TO MERGE TO calmeanday.py output to a file
import glob, os
import pandas as pd

dir = f'D:/ARP/data_2018/temp/'
output = f'{dir}/../transform/'
if not os.path.isdir(output):
    os.mkdir(output)

all_files = glob.glob(dir + "/*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files))
df = df.reset_index(drop=True, inplace=True)
df.to_csv(f'wholeyear.csv', index = False)