from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit
import sys

class mainwindow(QtGui.QWidget):
	def __init__(self):
		super(mainwindow, self).__init__()
		self.defaultWidth = 800
		self.defaultHeight = 600
		self.__initUI__()
		pass
	def __initUI__(self):
		self.MainVLayout = QtGui.QVBoxLayout()
		self.MainHLayout = QtGui.QHBoxLayout()
		
		self.Tab1Widget = QtGui.QWidget()
		
		self.MainTabWidget = QtGui.QTabWidget()
		
		self.MainVLayout.addWidget(self.MainTabWidget)
		self.setLayout(self.MainVLayout)
		self.show()
		pass
	