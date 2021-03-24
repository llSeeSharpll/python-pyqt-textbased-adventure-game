from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import intro

class SurviveWindow(QWidget):
    def __init__(self,surive_type, parent = None):
        super(SurviveWindow, self).__init__(parent)
        self.setGeometry(450,300,400,400)

        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setPixelSize(12)

        if(surive_type=="town"):
            surviveLabel = QLabel("You quickly hold out the purple flower, somehow hoping it will stop the orc.\nIt does! The orc was looking for love.\nThis got weird, but you survived!",self)
            surviveLabel.setFont(myFont)
            surviveLabel.setGeometry(10,0,400,100)

        if(surive_type=="orc"):
            surviveLabel = QLabel("You laid in wait. The shimmering sword attracted the orc, which thought you were no match.\nAs he walked closer and closer, your heart beat rapidly.\nAs the orc reached out to grab the sword, you pierced the blade into its chest.\nYou survived!",self)
            surviveLabel.setFont(myFont)
            surviveLabel.setGeometry(10,0,400,100)

        

        openButton = QPushButton("Start a New Story",  self)
        openButton.setGeometry(0,100,250,50)
        openButton.clicked.connect(self.openSub)

        closeButton = QPushButton("Quit",self)
        closeButton.setGeometry(0,150,250,50)
        closeButton.clicked.connect(self.close)


    def closeEvent(self, event):
        event.accept()
    
    def openSub(self):
        self.sub = intro.IntroWindow()
        self.close()
        self.sub.show()