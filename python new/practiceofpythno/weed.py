from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWin(QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.setGeometry(150, 150, 1000, 700)
        self.setWindowTitle('Akij Biri')
        self.initUI()
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Akij bhai ganza bhai')
        self.label.setGeometry(100, 100, 400, 400)
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(100, 100, 300, 100)
        self.btn1.clicked.connect(self.press)
        self.btn1.setText('Press for ganja!')
    def press(self):
        self.label.setText('You Clicked the button!')
        self.update()
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()
    sys.exit(app.exec_())
window()

