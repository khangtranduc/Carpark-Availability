import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import glob, os

ROOT = 'D:/CompSci/Projects/Python/ARP-Project/resources'
OUT = f'{ROOT}/out'

def rem_sp(dir):
    with open(dir) as big_guy:
        bg_l = pd.read_csv(big_guy).drop('Unnamed: 0', axis=1)
        out = f'{big_guy.name[:(77-13)]}.csv'
        bg_l.to_csv(out, index = False)
        print (out)
    os.remove(dir)

if __name__ == '__main__':
    t1 = datetime.now()
    years = ['2020', '2019', '2018']
    for y in years:
        names = glob.glob(f'{ROOT}/{y}/*.csv')
        for n in names:
            if ('=' not in n):
                continue
            rem_sp(n)

    print (f'{datetime.now() - t1}')