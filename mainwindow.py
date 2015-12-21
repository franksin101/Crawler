from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit
from PySide import QtNetwork
import gc
import sys
from QtHelper import QtLayoutCleanHandler

class mainwindow(QtGui.QWidget):
	def __init__(self):
		super(mainwindow, self).__init__()
		self.defaultWidth = 800
		self.defaultHeight = 600
		self.setWindowTitle("Crawler ver 1.0.0")
		self.webPageList = []
		self.__initUI__()
		pass
		
	def __initUI__(self):
		self.MainVLayout = QtGui.QVBoxLayout()
		self.MainHLayout = QtGui.QHBoxLayout()
		
		self.SubOtherHLayout = QtGui.QHBoxLayout()
		self.SubOtherVLayout = QtGui.QVBoxLayout()
		
		self.Tab1Widget = QtGui.QWidget()
		
		self.MainTabWidget = QtGui.QTabWidget()
		
		self.MainWebView = QtWebKit.QWebView()
		
		# self.MainWebView.load(QtCore.QUrl("http://www.tpa.edu.tw/tpaedu/Home/login.asp"))
		# self.MainWebView.load(QtCore.QUrl("https://ecourse.ccu.edu.tw/"))
		self.MainWebView.load(QtCore.QUrl("http://www.cs.ccu.edu.tw/~csasoc/drupal/"))
		self.MainWebView.show()
		
		self.MainWebView.loadFinished.connect(self.getPageData)
		self.MainWebView.linkClicked.connect(self.clickedToNewPage)
		
		self.MainTabWidget.addTab(self.MainWebView, "Web View")
		
		self.MainHLayout.addLayout(self.SubOtherVLayout)
		self.MainHLayout.addWidget(self.MainTabWidget)
		self.setLayout(self.MainHLayout)
		self.show()
		pass
		
	def getPageData(self, isFinished):
		if isFinished :
			#print(self.MainWebView.page().mainFrame().toHtml().encode("utf8"))
			print(self.MainWebView.page().mainFrame().documentElement().firstChild().tagName())
			print(self.MainWebView.page().mainFrame().childFrames())
			
			inputs = self.MainWebView.page().mainFrame().documentElement().findAll("input")
			forms = self.MainWebView.page().mainFrame().documentElement().findAll("form")

			print("MainFrame Frame Name is " + self.MainWebView.page().mainFrame().frameName())
			
			QtLayoutCleanHandler(self.SubOtherVLayout)
				
			for input in inputs :
				print((input.attribute("type"), input.attribute("name")))
				tmpHBoxLayout = QtGui.QHBoxLayout()
				if input.attribute("type") == u"submit" or input.attribute("type") == "submit" :
					print("get submit")
					self.SubOtherVLayout.addWidget(QtGui.QPushButton(input.attribute("value")))
				elif not input.attribute("type") == u"hidden" :
					tmpHBoxLayout.addWidget(QtGui.QLabel(input.previousSibling().toPlainText() + input.attribute("name")))
					tmpHBoxLayout.addWidget(QtGui.QLineEdit(input.attribute("value")))
					self.SubOtherVLayout.addLayout(tmpHBoxLayout)
			
			for frame in self.MainWebView.page().mainFrame().childFrames() : # find all child frames
				print("Frame Name is " + frame.frameName()) # get all frames' name
				inputs = frame.documentElement().findAll("input")
				for input in inputs :
					print((input.attribute("type"), input.attribute("name")))
					tmpHBoxLayout = QtGui.QHBoxLayout()
					if input.attribute("type") == u"submit" or input.attribute("type") == "submit" :
						print("get submit")
						self.SubOtherVLayout.addWidget(QtGui.QPushButton(input.attribute("value")))
					elif not input.attribute("type") == u"hidden" :
						tmpHBoxLayout.addWidget(QtGui.QLabel(input.attribute("name")))
						tmpHBoxLayout.addWidget(QtGui.QLineEdit(input.attribute("value")))
						self.SubOtherVLayout.addLayout(tmpHBoxLayout)
					
			self.SubOtherVLayout.update()
			
	def clickedToNewPage(self, url) :
		print("0.0")
		
		request = QtNetwork.QNetworkRequest()
		request.setRawHeader(
			"User-Agent",
			"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
		);
		request.setUrl(QtCore.QUrl(url))
		page = QtWebkit.QWebPage()
		self.webPageList.append(page)
		self.MainWebView.setPage(page)
		self.MainWebView.load(request)
		
		
			


			
			
		
	