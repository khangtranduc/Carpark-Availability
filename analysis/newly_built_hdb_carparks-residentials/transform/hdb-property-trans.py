import pandas as pd

hdb = pd.read_csv("D:\ARP\VISUALISATION\hdb-property-information\hdb-property-information.csv")
#hdb = hdb[['blk_no', 'street', 'year_completed', 'residential','commercial','market_hawker','miscellaneous','multistorey_carpark','precinct_pavilion','bldg_contract_town','total_dwelling_units']] ## get all property types including precint pavilion & miscellaneous & hawker centres
hdb = hdb[['blk_no', 'street', 'year_completed', 'residential', 'multistorey_carpark', 'bldg_contract_town','total_dwelling_units']]
hdb = hdb.loc[~(hdb['year_completed'] < 2017 ) ]
hdb = hdb.loc[~(hdb['residential'] == 'N' ) | ~(hdb['multistorey_carpark'] == 'N')]
hdb = hdb.sort_values(['year_completed', 'bldg_contract_town'], ascending=[1,1])
hdb.reset_index(drop=True, inplace=True)


print (hdb)
a = 2021
hdb = hdb[hdb.year_completed==a]
hdb.to_csv(f'hdb-resident-or-carpark-{a}.csv')