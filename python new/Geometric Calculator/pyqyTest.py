import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
import sys

def button_one_clicked():
    label_one.setText('Button has been clicked!')


app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(500, 300, 1280, 720)
win.setWindowTitle('Simple PyQT5 Program')
win.setWindowIcon(QtGui.QIcon('programming ideas.png'))

label_one = QtWidgets.QLabel(win)
label_one.setText('Wassap')
label_one.setFont(QtGui.QFont('Helvetica', 20))
label_one.setGeometry(200, 200, 500, 300)
label_one.move(100, 100)
label_one.show()

button_one = QtWidgets.QPushButton(win)
button_one.setText('Clicc Me!')
button_one.setFont(QtGui.QFont('Helvetica', 18))
button_one.setGeometry(300, 300, 200, 200)
button_one.move(310, 310)
button_one.clicked.connect(button_one_clicked)
button_one.show()






win.show()
sys.exit(app.exec_())
