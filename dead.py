from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import intro

class DeadWindow(QWidget):
    def __init__(self,dead_type ,parent = None):
        super(DeadWindow, self).__init__(parent)
        self.setGeometry(450,300,400,400)

        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setPixelSize(12)

        if(dead_type=="intro"):
            DeadLabel = QLabel("Welp, that was quick.\nYou died!",self)
            DeadLabel.setFont(myFont)
            DeadLabel.setGeometry(10,0,400,100)
        
        if(dead_type=="orc"):
            DeadLabel = QLabel("You decided to throw another rock,\nas if the first rock thrown did much damage.\nThe rock flew well over the orcs head.You missed.\nYou died!",self)
            DeadLabel.setFont(myFont)
            DeadLabel.setGeometry(10,0,400,100)
        
        if(dead_type=="cave"):
            DeadLabel = QLabel("Really? You're going to hide in the dark?\nI think orcs can see very well in the dark, right?\nNot sure,but I'm going with YES, so...\nYou died!",self)
            DeadLabel.setFont(myFont)
            DeadLabel.setGeometry(10,0,400,100)
        
        if(dead_type=="fight"):
            DeadLabel = QLabel("You should have picked up that sword.\nYou're defenseless. \nYou died!",self)
            DeadLabel.setFont(myFont)
            DeadLabel.setGeometry(10,0,400,100)

        if(dead_type=="run_Spoted"):
            DeadLabel = QLabel("You're easily spotted.\nYou died!",self)
            DeadLabel.setFont(myFont)
            DeadLabel.setGeometry(10,0,400,100)
        
        if(dead_type=="run_Fight"):
            DeadLabel = QLabel("You're no match for an orc.\nYou died!",self)
            DeadLabel.setFont(myFont)
            DeadLabel.setGeometry(10,0,400,100)
        
        if(dead_type=="no_flower"):
            DeadLabel = QLabel("You're should have picked up the Flowe\nYou died!",self)
            DeadLabel.setFont(myFont)
            DeadLabel.setGeometry(10,0,400,100)

        openButton = QPushButton("Start a New Story",  self)
        openButton.setGeometry(0,100,250,50)
        openButton.clicked.connect(self.openSub)

        closeButton = QPushButton("Quit",self)
        closeButton.setGeometry(0,150,250,50)
        closeButton.clicked.connect(self.close)


    def openSub(self):
        self.sub = intro.IntroWindow()
        self.close()
        self.sub.show()

    def closeEvent(self, event):
        event.accept()