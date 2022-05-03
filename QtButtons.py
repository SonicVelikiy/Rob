from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys
from PyQt5.uic.properties import QtGui
from PyQt5 import QtCore


class Window(QMainWindow):
    def __int__(self):
        super().__init__()
        title = "Telerob"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "example.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.UiComponents()
        self.show()


    def UiComponents(self):
        button = QPushButton("Click me", self)
        button.setGeometry(QRect(100, 100, 111, 28))
        button.setIcon(QtGui.QIcon("example.png"))
        button.setIconSize(QtCore.QSize(20, 20))
        button.setToolTip("This example")


