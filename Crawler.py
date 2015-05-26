__author__ = 'lpalonek'

import urllib.request as urllib
from bs4 import BeautifulSoup
import csv



class Crawler:
	baseUrl = 'http://prezydent2015.pkw.gov.pl/325_Wyniki_Polska/'
	results = list()

	def iterateOverPages(self):
		counter = 0
		for province in range(1, 30):
			for county in range(1, 50):
				for commune in range(1, 50):
					suffix = self.addZeroPrefix(province)+self.addZeroPrefix(county)+self.addZeroPrefix(commune)
					url = self.baseUrl+suffix
					if self.isAdressCorrect(url):
						self.findAllData(url)
					else:
						c = commune
						break
				if c == 1:
					break



	def addZeroPrefix(self, number):
		if number < 10:
			return '0'+str(number)
		else:
			return str(number)

	def findAllData(self, url):
		data = urllib.urlopen(url).read()
		data = BeautifulSoup(data)
		nameResult = self.findNamesAndResults(data)
		commune = self.findCommune(data)
		result = commune+','+nameResult[0]+','+nameResult[1]+','+nameResult[2]+','+nameResult[3]
		self.results.append(result)

	def findNamesAndResults(self, data):
		tag = data.find("div", {"id": "wyniki1_tabela_osoby_prawo"})
		winnerName = tag.findAll("a")[1].contents[0]
		loserName = tag.findAll("a")[4].contents[0]
		winnerResult = tag.findAll("a")[2].contents[0]
		loserResult = tag.findAll("a")[5].contents[0]
		return (winnerName, winnerResult, loserName, loserResult)

	def findCommune(self, data):
		tag = data.find("div", {"id": "wyniki1_droga"})
		commune = tag.findAll("li")[4].contents[0].contents[0]
		return commune

	def isAdressCorrect(self, url):
		data = urllib.urlopen(url).read()
		data = BeautifulSoup(data)
		tag = data.find("div", {"id": "wyniki1_tabela_osoby_prawo"})
		if int(tag.findAll("a")[2].contents[0]) > 0:
			return True
		else:
			return False

	def writeFile(self):
		writer = csv.writer(open('election.csv', 'w'))
		for row in self.results:
			writer.writerow([row])





craw = Crawler()
craw.iterateOverPages()
craw.writeFile()
