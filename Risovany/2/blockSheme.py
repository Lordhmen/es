import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    # Заполнение фигуры (0 - белый, 1 - черный)
    brush = [QBrush(Qt.white), QBrush(Qt.black)]

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 400, 500)
        self.setWindowTitle('Блок схема')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp, e)
        qp.end()

    def drawBrushes(self, qp, event):
        qp.setFont(QFont('Decorative', 10))
        qp.drawEllipse(160, 15, 140, 60)

        qp.drawText(208, 50, "Вызов")

        qp.drawLine(230, 75, 230, 100)

        qp.drawRect(180, 100, 100, 50)

        qp.drawText(195, 130, "count = 0")

        qp.drawLine(230, 150, 230, 180)

        qp.drawLine(150, 180, 310, 180)
        qp.drawLine(150, 220, 310, 220)
        qp.drawLine(340, 200, 310, 220)
        qp.drawLine(340, 200, 310, 180)
        qp.drawLine(120, 200, 150, 220)
        qp.drawLine(120, 200, 150, 180)

        qp.drawText(175, 205, "i = 0; i < 5; i++")

        qp.drawLine(230, 220, 230, 250)

        qp.drawLine(230, 250, 170, 280)
        qp.drawLine(230, 310, 170, 280)
        qp.drawLine(230, 250, 290, 280)
        qp.drawLine(230, 310, 290, 280)

        qp.drawText(205, 285, "i%2=0")

        qp.drawLine(290, 320, 340, 320)
        qp.drawLine(270, 350, 320, 350)
        qp.drawLine(270, 350, 290, 320)
        qp.drawLine(340, 320, 320, 350)

        qp.drawText(295, 340, "i+1")

        qp.drawLine(130, 320, 180, 320)
        qp.drawLine(110, 350, 160, 350)
        qp.drawLine(110, 350, 130, 320)
        qp.drawLine(180, 320, 160, 350)

        qp.drawText(140, 340, "i")

        qp.drawLine(145, 320, 145, 280)
        qp.drawLine(145, 280, 170, 280)

        qp.drawLine(310, 320, 310, 280)
        qp.drawLine(310, 280, 290, 280)

        qp.drawText(290, 270, "False")
        qp.drawText(135, 270, "True")

        qp.drawLine(145, 350, 145, 370)
        qp.drawLine(310, 350, 310, 370)
        qp.drawLine(145, 370, 310, 370)

        qp.drawLine(225, 370, 225, 380)
        qp.drawLine(90, 380, 225, 380)
        qp.drawLine(90, 200, 90, 380)
        qp.drawLine(90, 200, 120, 200)

        qp.drawLine(340, 200, 370, 200)
        qp.drawLine(370, 390, 370, 200)
        qp.drawLine(225, 390, 370, 390)
        qp.drawLine(225, 390, 225, 400)

        qp.drawEllipse(160, 400, 140, 60)

        qp.drawText(208, 435, "Вызов")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
