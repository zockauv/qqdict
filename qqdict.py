import sys
import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow
from dictUI_v2 import *
import sqlite3 as sl3


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.means = []
        self.config = configparser.ConfigParser()
        self.config.read('setup.ini')

        try:
            self.setconfig()
        except KeyError:
            pass

        self.wordInput.textChanged.connect(self.lookup)
        self.wordInput.returnPressed.connect(self.mean)
        self.wordList.itemActivated['QListWidgetItem*'].connect(self.selected)
        self.menuSave.triggered.connect(self.save)
        self.menuAbout.triggered.connect(self.about)

    def about(self):
        message = "秋秋词典  版本号:0.2\n\n祝秋秋小宝宝快乐长大!\n"
        QtWidgets.QMessageBox.about(self, '关于', message)

    def setconfig(self):
        x = self.config['window'].getint('posx')
        y = self.config['window'].getint('posy')
        w = self.config['window'].getint('width')
        h = self.config['window'].getint('height')
        self.setGeometry(QtCore.QRect(x, y, w, h))
    
    def save(self):
        self.config['window'] = {'posx': self.geometry().x(),
                                 'posy': self.geometry().y(),
                                 'width': self.geometry().width(),
                                 'height': self.geometry().height()}

        with open('setup.ini', mode='w') as f:
            self.config.write(f)
            QtWidgets.QMessageBox.about(self, ' ', '保存完成')
    
    def selected(self, item):
        self.printMean(self.means[self.wordList.currentRow()])
        self.wordList.setMaximumHeight(0)
        self.wordInput.setFocus()
        self.wordInput.setText(item.text())
        self.wordInput.selectAll()
        self.wordList.setVisible(False)

    def lookup(self):
        self.wordList.clear()
        word = self.wordInput.text()
        if word == '':
            self.wordList.setVisible(False)
            return
        self.wordList.setVisible(True)
        results = cursor.execute("SELECT * FROM DICT WHERE lower(WORD) LIKE '{}%' LIMIT 5".format(word.lower()))
        words, self.means = [], []
        for t in results:
            words.append(t[0])
            self.means.append(t[1])
        for i, w in enumerate(words):
            item = QtWidgets.QListWidgetItem()
            self.wordList.addItem(item)
            item = self.wordList.item(i)
            item.setText(w)
        self.wordList.setMaximumHeight((self.wordList.sizeHintForRow(0)+2) * self.wordList.count())

    def mean(self):
        word = self.wordInput.text()
        if word == '':
            return
        result = cursor.execute("SELECT MEANING FROM DICT WHERE lower(WORD) = '{}'".format(word.lower()))
        try:
            t = next(result)[0]
        except StopIteration:
            try:
                t = self.means[0]
                self.wordInput.setText(self.wordList.item(0).text())
            except IndexError:
                self.wordInput.selectAll()
                return
        self.wordInput.selectAll()
        self.printMean(t)
        self.wordList.setMaximumHeight(0)
    
    def printMean(self, mean):
        m = mean.split('/&/')
        meaning = '\n'.join(m)
        try:
            self.wordText.setText(meaning)
        except UnboundLocalError:
            pass

conn = sl3.connect('db-simple.sqlite')
cursor = conn.cursor()

app = QApplication(sys.argv)
myWin = MyMainWindow()
myWin.show()
app.exec_()
conn.close()