from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import main_story
import dead
import town

class RunWindow(QWidget):
    def __init__(self,run_type, parent = None):
        super(RunWindow, self).__init__(parent)
        self.setGeometry(450,300,420,420)

        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setPixelSize(12)

        if(run_type=="orc"):
            runLabel = QLabel("As the orc enters the dark cave, you sliently sneak out.\nYou're several feet away, but the orc turns around and sees you running.",self)
            runLabel.setFont(myFont)
            runLabel.setGeometry(10,0,400,100)
            introLabel = QLabel(""+main_story.Option_Run.option_Run,self)
            introLabel.setFont(myFont)
            introLabel.setGeometry(10,30,400,100)
        else:
            introLabel = QLabel(""+main_story.Option_Run.option_Run,self)
            introLabel.setFont(myFont)
            introLabel.setGeometry(10,0,400,100)


        chioceAButton = QPushButton(""+main_story.Option_Run.choiceA,self)
        chioceAButton.setGeometry(10,120,300,50)
        chioceAButton.clicked.connect(self.openSub_A)
        chioceAButton.setStyleSheet("QPushButton { text-align: left; }")

        chioceBButton = QPushButton(""+main_story.Option_Run.choiceB,self)
        chioceBButton.setGeometry(10,170,300,50)
        chioceBButton.clicked.connect(self.openSub_B)
        chioceBButton.setStyleSheet("QPushButton { text-align: left; }")

        chioceCButton = QPushButton(""+main_story.Option_Run.choiceC,self)
        chioceCButton.setGeometry(10,220,300,50)
        chioceCButton.clicked.connect(self.openSub_C)
        chioceCButton.setStyleSheet("QPushButton { text-align: left; }")

    def closeEvent(self, event):
        event.accept()

    def openSub_A(self):
        self.sub = dead.DeadWindow("run_Spoted")
        self.close()
        self.sub.show()
    
    def openSub_B(self):
        self.sub = dead.DeadWindow("run_Fight")
        self.close()
        self.sub.show()
    
    def openSub_C(self):
        self.sub = town.TownWindow()
        self.close()
        self.sub.show()