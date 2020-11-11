# coding: utf8
import sys
from FromXML import *

from PyQt5 import QtWidgets
import xml.dom.minidom

# Главный клас
class MyWin(QtWidgets.QMainWindow):
    # Конструктор
    def __init__(self, parent=None):
        # Вывод виджетов
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Обработка событий
        self.ui.pushButton.clicked.connect(self.XML)

    # Событие вывода
    def XML(self):
        # Считывание XML файла
        self.dom = xml.dom.minidom.parse("items.xml")
        # Разделение XML файла в массив
        self.items = self.dom.getElementsByTagName("items")
        # Вывод содержимого в текстовое поле
        self.ui.textEdit.insertHtml(self.items[0].attributes["item"].value)


# Запуск класса
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())