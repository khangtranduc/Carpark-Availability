data = pd.read_csv('PATH_TO_CARPARk_DATA')
g = data.groupby('time')
g = g.get_group((list(g.groups)[0]))
hdb = pd.read_csv('hdb-carpark-information.csv')
df = pd.merge(g,hdb,left_on='number',right_on='car_park_no')

geometric_points = []
for xy in zip(df['x_coord'], df['y_coord']):
   geometric_points.append(Point(xy))
gl = gpd.GeoDataFrame(df, crs = {'init': 'epsg:3414'}, geometry = geometric_points)
gl = gl.to_crs(4326)
gl=pd.DataFrame(gl)

r = []

for i in range(0, len(gl)):
   point = gl.geometry.loc[i]
   r.append(regions[regions.contains(point).values]['Area'].iloc[0])

gl['region']=r
gl.drop(df.columns[0],axis=1,inplace=True)
