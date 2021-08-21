import PyQt5
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import time

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QLabel,QPushButton
from PyQt5.QtGui import QPixmap

#import receiveimage



class Image_Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.show_image()

    def show_image(self):
        image = QPixmap("received.png")
        #print(image)
        self.label = QLabel(self)
        self.label.setPixmap(image)
        self.label.resize(1000,1000)

    def update(self):
        image = QPixmap("received.png")
        self.label.setPixmap(image)
        self.label.resize(1000,1000)




def main():
    app = QApplication(sys.argv)
    widget = Image_Widget()
    widget.resize(1000,1000)
    widget.show()

    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: widget.update())
    timer.start(1000) 

    app.exec_()







