from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit
import gc
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
		
		self.MainTabWidget.addTab(self.MainWebView, "first")
		
		self.MainHLayout.addLayout(self.SubOtherVLayout)
		self.MainHLayout.addWidget(self.MainTabWidget)
		self.setLayout(self.MainHLayout)
		self.show()
		pass
		
	def getPageData(self, isFinished):
		if isFinished :
			print(self.MainWebView.page().mainFrame().toHtml().encode("utf8"))
			print(self.MainWebView.page().mainFrame().documentElement().firstChild().tagName())
			print(self.MainWebView.page().mainFrame().childFrames())
			
			inputs = self.MainWebView.page().mainFrame().documentElement().findAll("input")
			
			test
			
			print("MainFrame Frame Name is " + self.MainWebView.page().mainFrame().frameName())
			
			while self.SubOtherVLayout.itemAt(0) :
				self.SubOtherVLayout.removeWidget(self.SubOtherVLayout.itemAt(0).widget())
			self.SubOtherVLayout.update()
				
			for input in inputs :
				print((input.attribute("type"), input.attribute("name")))
				self.SubOtherVLayout.addWidget(QtGui.QPushButton(input.attribute("type")))
			
			for frame in self.MainWebView.page().mainFrame().childFrames() : # find all child frames
				print("Frame Name is " + frame.frameName()) # get all frames' name
				inputs = frame.documentElement().findAll("input")
				for input in inputs :
					print((input.attribute("type"), input.attribute("name")))
					self.SubOtherVLayout.addWidget(QtGui.QPushButton(frame.frameName() + " " + input.attribute("type")))
			
		
	