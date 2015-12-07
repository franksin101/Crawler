from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit
import sys

class mainwindow(QtGui.QWidget):
	def __init__(self):
		super(mainwindow, self).__init__()
		self.defaultWidth = 800
		self.defaultHeight = 600
		self.setWindowTitle("Crawler ver 1.0.0")
		self.__initUI__()
		pass
	def __initUI__(self):
		self.MainVLayout = QtGui.QVBoxLayout()
		self.MainHLayout = QtGui.QHBoxLayout()
		
		self.Tab1Widget = QtGui.QWidget()
		
		self.MainTabWidget = QtGui.QTabWidget()
		
		self.MainWebView = QtWebKit.QWebView()
		#self.MainWebRequest = QtNetwork
		self.MainWebView.load(QtCore.QUrl("http://www.tpa.edu.tw/tpaedu/Home/login.asp"))
		self.MainWebView.show()
		
		self.MainWebView.loadFinished.connect(self.getPageData)
		
		self.MainTabWidget.addTab(self.MainWebView, "first")
		
		self.MainVLayout.addWidget(self.MainTabWidget)
		self.setLayout(self.MainVLayout)
		self.show()
		pass
	def getPageData(self, isFinished):
		if isFinished :
			print(self.MainWebView.page().mainFrame().toHtml().encode("utf8"))
			print(self.MainWebView.page().mainFrame().documentElement().firstChild().tagName())
			print(self.MainWebView.page().mainFrame().childFrames())
			for frame in self.MainWebView.page().mainFrame().childFrames() :
				print(frame.frameName())
		
	