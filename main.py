import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import intro

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Story Adventure")
        self.setGeometry(450,300,250,200)

        mainLabel = QLabel("Welcome\n Sart a new adventure",self)
        mainLabel.setGeometry(10,0,150,50)


        openButton = QPushButton("Start a New Story",  self)
        openButton.setGeometry(0,50,250,50)
        openButton.clicked.connect(self.openSub)

        closeButton = QPushButton("Quit",self)
        closeButton.setGeometry(0,100,250,50)
        closeButton.clicked.connect(self.close)


    def openSub(self):
        self.sub = intro.IntroWindow()
        self.close()
        self.sub.show()


    def closeEvent(self,event):
        event.accept()



def main():
    app = QApplication(sys.argv)
    mainWin =MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()