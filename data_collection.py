import pandas as pd
import numpy as np
from arraylist import arraylist
import requests
from datetime import datetime, timedelta

def fetch(d: datetime):
  response = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability?date_time=' + d.strftime("%Y-%m-%dT%H%%3A%M%%3A%S"))
  json_data = response.json()
  print (response)
  if response.status_code == 504:
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
    print ('--------- Span time:  %s --------' % (datetime.now() - tspan))
    df = pd.DataFrame(arr, columns=['number','time','total', 'available'])
    t -= inte
    with open(f'D:/ARP/data/{t.strftime("%Y-%m-%d=%H+%M+%S")}.csv', 'w') as csv_file:
      df.to_csv(path_or_buf=csv_file)
  print ('--------- stream time:  %s --------' % (datetime.now() - tstream))


if __name__ == "__main__":
  t1 = datetime.now()
  stream(t1, timedelta(days = 7), timedelta(days = 1))
  # for i in range(1000):
  #   print(i)
  #   fetch(t1 - timedelta(minutes=i))
  print ((datetime.now() - t1)/1000)