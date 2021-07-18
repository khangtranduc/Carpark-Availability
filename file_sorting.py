import pandas as pd
import glob, os
from datetime import datetime

ti1 = datetime.now()
print(ti1)

dir = 'D:/ARP/data_2021'
output = f'{dir}/output/'

if not os.path.isdir(output):
    os.mkdir(output)

files = glob.glob(f"{dir}/*.csv")
first=pd.read_csv(files[0])
first = first.loc[:, ~first.columns.str.contains('^Unnamed')]
fdate=first.time.str.split(' ').str.get(0).unique()[1]
a = first[first.time.str.split(' ').str.get(0)==fdate]
a.drop_duplicates()
a.to_csv(output+fdate+'.csv',index=False)

for i in range(0,len(files)-1) :
    file1=pd.read_csv(files[i])
    file2=pd.read_csv(files[i+1])
    df = file2.append(file1)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    date=df.time.str.split(' ').str.get(0)
    dates = date.unique()
    b = df[df.time.str.split(' ').str.get(0)==dates[1]]
    b = b.drop_duplicates()
    b.to_csv(output+dates[1]+'.csv',index=False)

last=pd.read_csv(files[len(files)-1])
last = last.loc[:, ~last.columns.str.contains('^Unnamed')]
ldate=last.time.str.split(' ').str.get(0).unique()[0]
c = last[last.time.str.split(' ').str.get(0)==ldate]
c.drop_duplicates()
c.to_csv(output+ldate+'.csv',index=False)

print ('----------------------- Total runtime:  %s ------------------' % (datetime.now() - ti1))
