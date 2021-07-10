import pandas as pd
import numpy as np
from arraylist import arraylist
import requests
import os
import time
from datetime import datetime, timedelta

def fetch(d: datetime):
  try:
    response = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability?date_time=' + d.strftime("%Y-%m-%dT%H%%3A%M%%3A%S"), timeout = 4)
  except:
    print ('timed out')
    return fetch(d)
  json_data = response.json()
  print (response)
  if response.status_code == 504 or response.status_code == 500 or response.status_code == 502:
    return fetch(d)

  carpark_data = json_data['items'][0]['carpark_data']
  csv_l = arraylist()
  for i in carpark_data:
    row = [i['carpark_number'],d.strftime("%Y-%m-%d %H:%M:%S"),i['carpark_info'][0]['total_lots'],i['carpark_info'][0]['lots_available']]
    csv_l.update(row)

  return csv_l.finalize()

def span(start: datetime, ran: timedelta, incre: timedelta):
  end = start - ran
  i = start
  csv_l = np.empty(4, dtype=object)
  
  while i >= end:
    if (i.strftime('%H%M') == '0000'):
      i += timedelta(minutes = 1)
    a_l = fetch(i)
    i -= incre
    csv_l = np.vstack((csv_l, a_l))
  return csv_l[1:]
 
def stream(start: datetime, dend: timedelta, inte: timedelta):
  tstream = datetime.now()
  end = start - dend
  t = start
  while t >= end:
    tspan = datetime.now()
    arr = span(t, inte, timedelta(minutes = 5))
    print ('---------------------- Span time:  %s ---------------------' % (datetime.now() - tspan))
    df = pd.DataFrame(arr, columns=['number','time','total', 'available'])
    t -= inte
    with open(f'D:/ARP/data/{t.strftime("%Y-%m-%d=%H+%M+%S")}.csv', 'w') as csv_file:
      df.to_csv(path_or_buf=csv_file)
  print ('----------------------- stream time:  %s ------------------' % (datetime.now() - tstream))

import os

def newest(path):
  files = os.listdir(path)
  paths = [os.path.join(path, basename) for basename in files]
  base=os.path.basename(max(paths, key=os.path.getctime))
  return os.path.splitext(base)[0]

if __name__ == "__main__":
  while True:
    print(datetime.now)
    dateti = newest(f'D:\ARP\data')
    # time = input('Enter time: ')
    print (f'Getting date: {dateti}')
    t1 = datetime.strptime(dateti, '%Y-%m-%d=%H+%M+%S')
    stream(t1, timedelta(days = 3), timedelta(days = 1))
    time.sleep(480)
    print(datetime.now)