import re
import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
import sys

class Lecture(object):
	def __init__(self, url):
		self.url = url
		html = urlopen(exampleLecture).read()
		soup = bs(html)
		self.date = self.getDate(soup)
		self.title = self.getTitle(soup)
		self.speaker = self.getSpeakerInfo(soup)[0]
		self.org = self.getSpeakerInfo(soup)[1]
		self.desc = self.getDesc(soup)
		self.srt = self.getSrt(soup)
	
	def getDate(self, soup):
		date = soup.find("td",{"align":"right"}).getText().strip()
		return date
	
	def getTitle(self, soup):
		title = soup.findAll("td", {"class":"r2010_mid_header_first_row"})[0].getText().strip()
		return title
		
	def getSpeakerInfo(self, soup):
		regex = re.compile(r'[Stanford\'s\sEntrepreneurship\sCorner:]\s(\w+[\s\w+]+?)[,]\s(\S+)\s-') 
		titleLine = re.findall(regex, soup.find("title").getText())[0]
		return titleLine
	
	def getDesc(self, soup):
		desc = soup.find('div',{'id':"description_div"}).getText()
		return desc
	
	def getSrt(self, soup):
		transcript = soup.find('meta',{'itemprop':"transcript"})
		if transcript:
			return True
		else:
			return False
	
	def printTranscript(self, soup):
		if self.srt == True:
			print soup.find('meta',{'itemprop':"transcript"})
		else:
			return False

###Example instance below
exampleLecture = "http://ecorner.stanford.edu/authorMaterialInfo.html?mid=2351"

def main(url):
	newLec = Lecture(url)
	print newLec.date
	print newLec.title
	print newLec.speaker
	print newLec.org


if __name__ == '__main__':
	main(sys.argv)
	
