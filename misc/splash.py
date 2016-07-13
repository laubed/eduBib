import sys
import os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    
    def __init__(self):
        
  
        QtGui.QWidget.__init__(self,parent = None,flags=QtCore.Qt.FramelessWindowHint)
        self.layout= QtGui.QVBoxLayout(self)
        self.setWindowTitle('eduBib')
        self.setGeometry(200,200,844,344)
        self.setWindowIcon(QtGui.QIcon('eduBibLogo.png'))
        self.pic = QtGui.QLabel(self)
        text = None
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd()+"/splash.png"))
        self.pic.setGeometry(0,0,844,344)

        self.addText('Lade...')
        self.show()
    def run(self):
        
        app = QtGui.QApplication(sys.argv)
        app.exec_()
        self.show()
    def addText(self,text):
        self.text = QtGui.QLabel(text,self)
        self.text.setFont(QtGui.QFont("Arial", 32))
        self.a = 500
        self.b= 600
        
        self.text.setGeometry(350,0,self.a,self.b)
        
app = QtGui.QApplication(sys.argv)
window = Window()
window.run()
