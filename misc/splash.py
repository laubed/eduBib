#imports
import sys
import os
from PyQt4 import QtGui
import time 
class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.a = 50
        self.b = 50
        self.c = 500
        self.d = 300
        self.setGeometry(self.a,self.b,self.c,self.d)
        self.setWindowTitle("eduBib")
        self.background= QtGui.QLabel
        self.setBackground("splash.png")
        self.textbox =QtGui.QTextEdit()
    def setBackground(self,address):
        self.background.setGeometry(self.a,self.b,self.c,self.d)
        self.background.setPixmap(os.getcwd()+"/splash.png")
    
    def setText(self,message):
        self.textbox.append(message)
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    window = window()
    window.setText('Creating Databases')
    window.show()
    sys.exit(app.exec_())
        
