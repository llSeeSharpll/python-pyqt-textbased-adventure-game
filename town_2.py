from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import main_story
import dead
import survive

class TownWindow(QWidget):
    def __init__(self, parent = None):
        super(TownWindow, self).__init__(parent)
        self.setGeometry(450,300,400,400)

        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setPixelSize(12)


        introLabel = QLabel(""+main_story.Option_Town_2.option_Town_2,self)
        introLabel.setFont(myFont)
        introLabel.setGeometry(10,0,400,100)


        chioceAButton = QPushButton(""+main_story.Option_Town_2.choiceA,self)
        chioceAButton.setGeometry(10,120,300,50)
        chioceAButton.clicked.connect(self.openSub_A)
        chioceAButton.setStyleSheet("QPushButton { text-align: left; }")


        chioceBButton = QPushButton(""+main_story.Option_Town_2.choiceB,self)
        chioceBButton.setGeometry(10,170,300,50)
        chioceBButton.clicked.connect(self.openSub_B)
        chioceBButton.setStyleSheet("QPushButton { text-align: left; }")

        chioceCButton = QPushButton(""+main_story.Option_Town_2.choiceC,self)
        chioceCButton.setGeometry(10,220,300,50)
        chioceCButton.clicked.connect(self.openSub_C)
        chioceCButton.setStyleSheet("QPushButton { text-align: left; }")

    def closeEvent(self, event):
        event.accept()

    def openSub_A(self):
        if main_story.flower>0:
            self.sub = survive.SurviveWindow("town")
            self.close()
            self.sub.show()
        else:
            self.sub = dead.DeadWindow("no_flower")
    
    def openSub_B(self):
        self.sub = dead.DeadWindow("run_Spoted")
        self.close()
        self.sub.show()

    def openSub_C(self):
        self.sub = dead.DeadWindow("run_Fight")
        self.close()
        self.sub.show()