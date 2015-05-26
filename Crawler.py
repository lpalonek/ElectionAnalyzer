__author__ = 'lpalonek'

import urllib.request as urllib

class Crawler:
	baseAddress = 'http://prezydent2015.pkw.gov.pl/325_Wyniki_Polska/'

	def iterateOverPages(self):
		page = urllib.urlopen(self.baseAddress)
		result = page.read()
		print(result)
		print("www")
		print("www")




craw = Crawler()
craw.iterateOverPages()