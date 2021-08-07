# Carpark-Availability
ARP carpark vry cool

# Resources
https://docs.google.com/document/d/1js3wSzBERYVraM8yzfece3nW-QNQ9zPNM3AEA11_G5Q/edit
<br />Markdown Cheatsheet: https://github.com/tchapi/markdown-cheatsheet

# Documentation
## Apis:
#### Carpark Availability: https://data.gov.sg/dataset/carpark-availability
The API can best receive 4 days of data in a row
the next day there will be too much timeout
Better set sleep time of 13 mins in between calls for better runtime

eg:<br /> 	1st day -- 5 mins<br />
	2st day -- 5 mins<br />
	3rd day -- 7 mins<br />
	4th day -- 8 mins<br />
	5th day -- 15 mins<br />

# Data Transformations
## Naming conventions:
trans_m_pd_pc : transformed - mean(value) - per day - per carpark
trans_s_pm_a : transformed - sum(value) - per month - all carparks

## Scripts usage
### calmeanday.py take processed data
### merge_all.py takes output files from calmeanday.py
### calsummonth.py take output file from merge_all.py
