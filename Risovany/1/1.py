import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = 'Я люблю Python'
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()

    # Класс QPainter отвечает за все низкоуровневое рисование.
    # Все методы рисования идут между методами begin() и end().
    # Фактическое рисование делегируется пользовательскому методу drawText().

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    # Метод drawText() рисует текст в окне.
    # Метод rect() собития рисования

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 6))  # Установка ручки
        qp.setFont(QFont('Decorative', 10))  # Установка шрифта
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)  # Выравниваем по центру


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
