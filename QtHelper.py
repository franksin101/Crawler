from PySide import QtCore
from PySide import QtGui

def QtLayoutCleanHandler(QLayoutObj) : 
	typeStr = str(type(QLayoutObj))
	print(QLayoutObj.count())
	while QLayoutObj.count() > 0:
		QLayoutObjItem = QLayoutObj.takeAt(0)
		if QLayoutObjItem.layout() :
			QtLayoutCleanHandler(QLayoutObjItem.layout())
			QLayoutObjItem.deleteLater()
		elif QLayoutObjItem.widget() :
			QLayoutObjItem.widget().deleteLater()
	print(QLayoutObj.count())
	QLayoutObj.update()