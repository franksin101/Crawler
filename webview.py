from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit
import sys

class webview(QtWebKit.QWebView):
	
	def __init__():
		super(webview, self).__init__()
	
	def __initUI__() :
		self.GobackButton = QtGui.QPushButton()
		self.ForwardButton = QtGui.QPushButton()
		self.PrintButton = QtGui.QPushButton()
		self.StopButton = QtGui.QPushButton()
		
		self.WebViewVLayout = QtGui.QVBoxLayout()
		self.WebViewHLayout = QtGui.QHBoxLayout()
		
		self.show()
	