from table import *
import sys
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

data = [['Python', 95.5], ['PHP', 55.1], ['Java', 5.29]]


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        global n, h
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        n = 4
        h = 2
        self.ui.tableWidget.setRowCount(n)
        self.ui.tableWidget.setColumnCount(h)

        self.ui.pushButton.clicked.connect(self.clear)
        self.ui.pushButton_2.clicked.connect(self.row)
        self.ui.pushButton_3.clicked.connect(self.column)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Язык', 'Знания'))
        line = 0
        for item in data:
            cellinfo = QTableWidgetItem(item[0])
            self.ui.tableWidget.setItem(line, 0, cellinfo)
            line += 1

    def clear(self):
        self.ui.tableWidget.clear()

    def row(self):
        global n
        n += 1
        self.ui.tableWidget.setRowCount(n)

    def column(self):
        global h
        h += 1
        self.ui.tableWidget.setColumnCount(h)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
