from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import main_story
import town_2

class TownWindow(QWidget):
    def __init__(self, parent = None):
        super(TownWindow, self).__init__(parent)
        self.setGeometry(450,300,400,400)

        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setPixelSize(12)


        introLabel = QLabel(""+main_story.Option_Town.option_Town,self)
        introLabel.setFont(myFont)
        introLabel.setGeometry(10,0,400,100)


        chioceAButton = QPushButton(""+main_story.Option_Town.choiceY,self)
        chioceAButton.setGeometry(10,120,300,50)
        chioceAButton.clicked.connect(self.openSub_A)
        chioceAButton.setStyleSheet("QPushButton { text-align: left; }")

        chioceBButton = QPushButton(""+main_story.Option_Town.choiceN,self)
        chioceBButton.setGeometry(10,170,300,50)
        chioceBButton.clicked.connect(self.openSub_B)
        chioceBButton.setStyleSheet("QPushButton { text-align: left; }")

    def closeEvent(self, event):
        event.accept()

    def openSub_A(self):
        self.sub = town_2.TownWindow()
        main_story.flower+=1
        self.close()
        self.sub.show()
    
    def openSub_B(self):
        self.sub = town_2.TownWindow()
        self.close()
        self.sub.show()