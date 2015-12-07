from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit
import sys
import mainwindow

if __name__ == "__main__" :
	print("the program is execute!")
	app = QtGui.QApplication(sys.argv)
	ui = mainwindow.mainwindow()
	sys.exit(app.exec_())

