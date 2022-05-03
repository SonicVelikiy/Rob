import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

import QtButtons

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("Telerob")




ui.show()
app.exec()





# def window():
#     app = QtWidgets.QApplication(sys.argv)
#     widget = QWidget()
#
#     button1 = QPushButton(widget)
#     button1.setText("Button1")
#     button1.setIcon("Robot.png")
#     button1.move(64, 32)
#     widget.setGeometry(50, 50, 320, 200)
#     widget.setWindowTitle("Example")
#     widget.show()
#     sys.exit(app.exec_())
# if __name__ == "__main__":
#     window()



