from menul import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.ui.action_5.triggered.connect(self.saveToFile)
        self.ui.action_7.triggered.connect(self.close)
        self.ui.action_8.triggered.connect(self.showDialog)

    def showDialog(self):
        options = QtWidgets.QFileDialog.Options()
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", "", "Текстовый файл(*.html)",
                                                                 options=options)
        if self.fileName:
            self.data = open(self.fileName, 'r', encoding='utf-8')
            self.ui.plainTextEdit.insertPlainText(self.data.read())
        self.data.close()

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Завершение работы",
                                                "Save text before quit?\nYou realy?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.saveToFile()
            e.accept()
        elif result == QtWidgets.QMessageBox.Cancel:
            e.ignore()
        else:
            e.accept()

    def saveToFile(self):
        options = QtWidgets.QFileDialog.Options()
        self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовый файл(*.html)",
                                                                 options=options)
        if self.fileName:
            self.writeFile = open(self.fileName, 'w', encoding='utf-8')
        self.writeFile.write(self.ui.plainTextEdit.toHtml())
        self.writeFile.close()
        self.ui.statusbar.showMessage("Save to %s" % self.fileName)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    ex = MyWin()
    sys.exit(app.exec_())
