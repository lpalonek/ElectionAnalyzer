__author__ = 'lpalonek'

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import shapefile
from CustomProjection import CP


cmap = mpl.cm.Blues
shapename = 'admin_0_countries'
countries_shp = shpreader.natural_earth(resolution='110m',
										category='cultural', name=shapename)
ax = plt.axes(projection=CP())

plt.axis('off')


countriesRecords = shpreader.Reader('/tmp/gminy/gminy.shp').records()
print("here")
counter = 0
for country in countriesRecords:
	country._shape
	ax.add_geometries(country.geometry, CP(),
					  facecolor=cmap(0.5, 1),
					  label='test', edgecolor='none')

	counter += 1
	break;
	if counter % 100 == 0:
		# break
		print(counter)


# for shape in shapefile.Reader(countries_shp).shapes():
# 	x,y = shape
# 	plt.plot(x,y)


	# ax.add_patch(PolygonPatch(poly, fc=colorConverter.to_rgba('r'), ec=colorConverter.to_rgba('r'), alpha=0.5, zorder=2 ))
# plt.show()
print("rendering map")
plt.savefig("map.png", dpi = 200)
