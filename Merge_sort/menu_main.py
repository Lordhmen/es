from os import system

from main import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.algoritm.clicked.connect(self.main_algoritm)
        self.ui.video.clicked.connect(self.video)
        self.ui.demo_sort.clicked.connect(self.demo_sort)
        self.ui.Exit.triggered.connect(self.close)

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Confirm Dialog", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def main_algoritm(self):
        system('main_algoritm.py')

    def video(self):
        system('Merge_sort.mp4')

    def demo_sort(self):
        system('main_merge_sort.py')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
