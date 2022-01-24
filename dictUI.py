
from PyQt5 import QtCore, QtWidgets, QtGui

class WordInput(QtWidgets.QLineEdit):
    def __init__(self, listWidget, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.listWidget = listWidget
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Down:
            if self.listWidget.count() > 0:
                self.listWidget.setFocus()
                self.listWidget.setCurrentRow(0)
        if event.key() == QtCore.Qt.Key_Escape:
            self.setText('')
        if event.key() == QtCore.Qt.Key_Space:
            return
        QtWidgets.QLineEdit.keyPressEvent(self, event)

class WordList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.focusNextChild()
        QtWidgets.QListWidget.keyPressEvent(self, event)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(150, 250))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setSpacing(0)
        self.stackLayout = QtWidgets.QStackedLayout()
        self.stackLayout.setContentsMargins(0,0,0,0)
        self.stackLayout.setStackingMode(1)
        self.wordText = QtWidgets.QTextBrowser(self.centralwidget)
        self.wordText.setObjectName("wordText")
        self.wordList = WordList(self.centralwidget)
        self.wordList.setObjectName("wordList")
        self.wordInput = WordInput(self.wordList, self.centralwidget)
        self.wordInput.setObjectName("wordInput")

        MainWindow.setTabOrder(self.wordInput, self.wordList)
        MainWindow.setTabOrder(self.wordList, self.wordText)
        self.wordText.setFocusPolicy(QtCore.Qt.NoFocus)

        self.stackLayout.addWidget(self.wordList)
        self.stackLayout.addWidget(self.wordText)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.wordInput)
        self.verticalLayout.addLayout(self.stackLayout)

        self.wordList.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.menuSwitchSimple = QtWidgets.QAction(MainWindow)
        self.menuSwitchSimple.setObjectName("menuSwitchSimple")
        self.menuOnTop = QtWidgets.QAction(MainWindow)
        self.menuOnTop.setObjectName("menuOnTop")
        self.menuExit = QtWidgets.QAction(MainWindow)
        self.menuExit.setObjectName("menuExit")
        self.menuAbout = QtWidgets.QAction(MainWindow)
        self.menuAbout.setObjectName("menuAbout")
        self.menuSave = QtWidgets.QAction(MainWindow)
        self.menuSave.setObjectName("menuSave")
        self.menu.addAction(self.menuSwitchSimple)
        self.menu_2.addAction(self.menuOnTop)
        self.menu_2.addAction(self.menuSave)
        self.menu_2.addAction(self.menuAbout)
        self.menu_2.addAction(self.menuExit)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "秋秋词典 Ver.0.2"))
        self.menu.setTitle(_translate("MainWindow", "数据库"))
        self.menu_2.setTitle(_translate("MainWindow", "程序"))
        self.menuSwitchSimple.setText(_translate("MainWindow", "简明英汉"))
        self.menuSave.setText(_translate("MainWindow", "保存设置"))
        self.menuAbout.setText(_translate("MainWindow", "关于"))
        self.menuExit.setText(_translate("MainWindow", "退出"))
        self.menuOnTop.setText(_translate("MainWindow", "切换置顶"))
