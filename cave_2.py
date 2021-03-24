from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import main_story
import run
import dead
import survive

class CaveWindow(QWidget):
    def __init__(self, parent = None):
        super(CaveWindow, self).__init__(parent)
        self.setGeometry(450,300,400,400)

        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setPixelSize(12)


        introLabel = QLabel(""+main_story.Option_Rock.option_Rock,self)
        introLabel.setFont(myFont)
        introLabel.setGeometry(10,0,400,100)


        chioceAButton = QPushButton(""+main_story.Option_Cave_2.choiceA,self)
        chioceAButton.setGeometry(10,120,300,50)
        chioceAButton.clicked.connect(self.openSub_A)
        chioceAButton.setStyleSheet("QPushButton { text-align: left; }")


        chioceBButton = QPushButton(""+main_story.Option_Cave_2.choiceB,self)
        chioceBButton.setGeometry(10,170,300,50)
        chioceBButton.clicked.connect(self.openSub_B)
        chioceBButton.setStyleSheet("QPushButton { text-align: left; }")

        chioceCButton = QPushButton(""+main_story.Option_Cave_2.choiceC,self)
        chioceCButton.setGeometry(10,220,300,50)
        chioceCButton.clicked.connect(self.openSub_C)
        chioceCButton.setStyleSheet("QPushButton { text-align: left; }")

    def closeEvent(self, event):
        event.accept()

    def openSub_A(self):
        self.sub = dead.DeadWindow("cave")
        self.close()
        self.sub.show()
    
    def openSub_B(self):
        if main_story.sword>0:
            self.sub = survive.SurviveWindow("orc")
            self.close()
            self.sub.show()
        else:
            self.sub = dead.DeadWindow("sword")
            self.close()
            self.sub.show()

    def openSub_C(self):
        self.sub = run.RunWindow("orc")
        self.close()
        self.sub.show()