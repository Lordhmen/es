from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Drawing Ellipse"
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 400

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 5, Qt.DashDotLine))
        # painter.setStyle(Qt.DashDotLine)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        # painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))

        painter.drawEllipse(100, 100, 400, 200)


        # pen = QPen(Qt.black, 2, Qt.SolidLine)
        # pen.setStyle(Qt.DashDotLine)
        # painter.setPen(pen)
        # painter.drawLine(20, 120, 250, 120)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())