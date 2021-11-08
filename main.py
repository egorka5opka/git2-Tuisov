import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5 import uic
from random import randint

MAX_R = 250


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle("Жёлтые круги")
        self.do_paint = False
        self.btn.clicked.connect(self.click)

    def click(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(Qt.yellow)
            qp.setBrush(Qt.yellow)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        d = randint(10, MAX_R) * 2
        x = randint(0, self.size().width() - d)
        y = randint(0, self.size().height() - d)
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
