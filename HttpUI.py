from PySide import *


HttpRequestHeaders = {  "Content-type": "application/x-www-form-urlencoded", 
						"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
						"Accept-Encoding": "gzip, deflate, sdch",
						"Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
						"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}

class HttpUI(QtGui.QWidget) :
	def __init__(self) :
		super(HttpUI, self).__init__()
		self.URL = ""
		self.UserAgent = ""
		self.initUI()

	def initUI(self) :
		vlayout = QtGui.QVBoxLayout(self)
		tabWidget = QtGui.QTabWidget()
		vlayout.addWidget(tabWidget)
		
		"""
			Request Tab Begin
		"""
		
		RequestTab = QtGui.QWidget()
		RequestTabLayout = QtGui.QVBoxLayout()
		
		
		SubmitLayout = QtGui.QHBoxLayout() 
		SubmitLabel = QtGui.QLabel("http://")
		self.SubmitLineEdit = QtGui.QLineEdit("www.example.com/index.php")
		self.SubmitPushButton = QtGui.QPushButton("Submit")
		
		self.SubmitLineEdit.textChanged.connect(self.urlChange)
		self.SubmitPushButton.clicked.connect(self.httpRequest)
		
		SubmitLayout.addWidget(SubmitLabel)
		SubmitLayout.addWidget(self.SubmitLineEdit)
		SubmitLayout.addWidget(self.SubmitPushButton)
		
		KVLayout = QtGui.QHBoxLayout()
		self.KVKeyLineEdit= QtGui.QLineEdit("Key")
		self.KVValueLineEdit= QtGui.QLineEdit("value")
		self.KVPushButton = QtGui.QPushButton("add")
		
		RequestTabLayout.addLayout(SubmitLayout)
		RequestTab.setLayout(RequestTabLayout)
		tabWidget.addTab(RequestTab, "Request")
		
		"""
			Request Tab End
		"""
		
		DOMTab = QtGui.QWidget()
		DOMTabLayout = QtGui.QVBoxLayout()
		DOMTab.setLayout(DOMTabLayout)
		
		tabWidget.addTab(DOMTab, "DOM")
		
		self.show()
	
	def urlChange(self) :
		self.URL = "http://" + self.SubmitLineEdit.text()
		print(self.URL)
	
	def httpRequest(self) :
		print("SUBMIT")
		pass
		