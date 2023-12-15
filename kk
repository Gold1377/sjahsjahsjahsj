#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit,QListWidget,QMessageBox
import json
#declaring constants
win_width, win_height = 200, 300
win_x, win_y = 200, 200
txt_title = "Sending text"
txt_line = "Entry field"
 
class SecWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # creating and customizing the graphical elements:
        self.initUI()
       
        #connects the elements
        self.connects()
        #determines how the window will look (text, size, location)
        self.set_appear()
 
        # start:
        
        
    def initUI(self):
        ''' creates graphical elements '''
        self.Q=QLabel()
        self.CC=QPushButton()
        self.VV=QPushButton()
        self.W=QPushButton()
        self.FF=QPushButton()
        gg=QVBoxLayout()
        gg.addWidget(self.Q)
        gg.addWidget( self.CC)
        gg.addWidget(self.VV)
        gg.addWidget(self.W)
        gg.addWidget(self.FF)
        self.setLayout(gg)
                
    def connects(self):
        
        # Nu need for the buttons to do something in this exercise/nothing to add here 
        pass
 
    ''' determines how the window will look (text, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
 
