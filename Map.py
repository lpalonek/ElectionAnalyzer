__author__ = 'lpalonek'

import matplotlib.pyplot as plt
import matplotlib as mpl

import csv

import custom.cartopy.shapereader as shpreader

from custom.CustomProjection import CP


class Map:
    def drawMap(self, csvFilename, plotFileName, color):
        cmap = color

        # ax = plt.axes(projection=CP())
        fig, ax = plt.subplots(figsize=(12,6),
                       subplot_kw={'projection': CP()})
        wrongRegions = []
        regionalResults = self.prepareRegionResults(csvFilename)
        colour = 1
        communeRecords = shpreader.Reader('/tmp/gminy.shp').records()
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
                # break;
                print(counter)

        norm = mpl.colors.Normalize(['Komor', 'Duda'])
        cax = fig.add_axes([0.313, 0.1, 0.399, 0.04])
        cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=mpl.colors.Normalize(clip=False), orientation='horizontal')
        cb.set_label('Komorowski                                                             Duda', rotation=0, labelpad=-50)


        print("rendering map")
        plt.savefig(plotFileName, dpi=600)

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
map.drawMap('election.csv', 'map8.png', mpl.cm.bwr)
map.drawMap('election.csv', 'map4.png', mpl.cm.gnuplot2)
map.drawMap('election.csv', 'map5.png', mpl.cm.jet)
map.drawMap('election.csv', 'map6.png', mpl.cm.winter)
map.drawMap('election.csv', 'map7.png', mpl.cm.cool)
map.drawMap('election.csv', 'map1.png', mpl.cm.rainbow)
map.drawMap('election.csv', 'map2.png', mpl.cm.seismic)
map.drawMap('election.csv', 'map3.png', mpl.cm.brg)
