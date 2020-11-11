import sys
import time
from itertools import permutations
from math import factorial

from guess import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.addItem('4')
        self.ui.comboBox.addItem('5')

        self.ui.statusbar.showMessage('Кирсанов Г.В.')

        self.ui.pushButton.clicked.connect(self.start1)

    def start1(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.Letters(self.ui.lineEdit.text(), int(self.ui.comboBox.currentText()))
        elif self.ui.comboBox.currentIndex() == 1:
            self.Letters(self.ui.lineEdit.text(), int(self.ui.comboBox.currentText()))

    def Letters(self, letters, n):
        time_programm = time.time()
        words = open("words.txt", "r", encoding="utf-8")
        textEdit = open("textEdit.txt", "w", encoding="utf-8")
        words_split = words.read().split()
        words.close()

        q = list(permutations(letters, r=n))
        podborov = factorial(n)
        n = 0
        letters_word = []
        for i in range(len(q)):
            q[n] = list(q[n])
            n += 1
        for i in q:
            spisok_words = ""
            for j in i:
                spisok_words += j
            letters_word.append(spisok_words)
        n = 1
        for i in letters_word:
            for j in words_split:
                if i == j:
                    print(n, j)
                    n += 1
        textEdit.write(
            "Время выполнения подбора: %d секунд \nКол-во проверенных комбинаций %d \nНайдено совпадений: %d\n" % (
            time_programm, podborov, n - 1))
        self.ui.plainTextEdit.appendPlainText(
            "Время выполнения подбора: %d секунд \nКол-во проверенных комбинаций %d \nНайдено совпадений: %d\n" % (
            time_programm, podborov, n - 1))
        self.ui.progressBar.setValue(100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
