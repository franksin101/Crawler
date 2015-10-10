import sys
import xml.etree.ElementTree as XMLParser
import urllib
import urllib.request as HttpRequest
from PySide import *
import HttpUI


HttpRequestHeaders = {  "Content-type": "application/x-www-form-urlencoded", 
						"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
						"Accept-Encoding": "gzip, deflate, sdch",
						"Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
						"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}

class POST :
	def __init__(self) :
		self.Data = {}
	def addData(self, key, value) :
		if not key in [e for e in self.Data.keys()] :
			self.Data[key] = value
			return True
		else :
			return False
	def removeData(self, key) :
		if key in [e for e in self.Data.keys()] :
			del self.Data[key]
			return True
		else :
			return False
	def data(self) :
		return urllib.parse.urlencode(self.Data)
	def dump(self) :
		for k in self.Data.keys() :
			print("%s | %s" % (k, self.Data[k]))
			
if __name__ == "__main__" :
	print("I am main function")
	
	app = QtGui.QApplication(sys.argv)
	
	ui = HttpUI.HttpUI()
	
	sys.exit(app.exec_())
	
	# req = HttpRequest.Request(url = "http://stackoverflow.com/questions/21394916/trouble-importing-dll-library-into-codeblocks-linker", headers = HttpRequestHeaders)
	# http = HttpRequest.urlopen(req)
	# print(http.read())
	# print(http.info())
	# print(http.geturl())
	
	