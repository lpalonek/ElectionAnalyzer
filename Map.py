__author__ = 'lpalonek'

import matplotlib.pyplot as plt
import matplotlib as mpl

import csv

import custom.cartopy.shapereader as shpreader

from custom.CustomProjection import CP


class Map:
	def drawMap(self, csvFilename):
		cmap = mpl.cm.cool
		ax = plt.axes(projection=CP())
		wrongRegions = []
		regionalResults = self.prepareRegionResults(csvFilename)
		colour = 1
		communeRecords = shpreader.Reader('/tmp/gminy/gminy.shp').records()
		counter = 0
		for commune in communeRecords:
			communeName = commune.attributes['jpt_nazwa_']
			if communeName in  regionalResults:
				colour = self.calculateColour(regionalResults[communeName])
			else:
				wrongRegions.append(communeName)
			ax.add_geometries(commune.geometry, CP(),
							  facecolor=cmap(colour, 1),
							  label='test', edgecolor='none')

			counter += 1
			if counter % 100 == 0:
				print(counter)
		print("rendering map")
		plt.savefig("map.png", dpi=200)

	def prepareRegionResults(self, csvFilename):
		csvFile = csv.reader(open(csvFilename))
		results = {}
		for row in csvFile:
			list = row[0].split(',')
			commune = list[0]
			if 'Duda' in list[1]:
				duda = dict(d=list[2])
				komor = dict(k=list[4])
			else:
				duda = dict(d=list[4])
				komor = dict(k=list[2])

			if results.__contains__(commune):
				duda2 = results[commune][0]
				komor2 = results[commune][1]
				duda = dict(d=int(duda2['d']) + int(duda['d']))
				komor = dict(k=int(komor2['k']) + int(komor['k']))
				results[commune][0] = duda
				results[commune][1] = komor
			else:
				list = []
				list.append(duda)
				list.append(komor)
				results[commune] = list

		return results

	def calculateColour(self, data):
		duda = int(data[0]['d'])
		komor = int(data[1]['k'])
		sum = duda + komor
		return duda / sum


map = Map()
map.drawMap('election.csv')
