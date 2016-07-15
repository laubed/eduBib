#imports
import sys
import os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    
    def __init__(self):
        
        
        super(Window,self).__init__()
       # QtGui.QWidget.__init__(self)
        self.layout =  QtGui.QVBoxLayout()
        self.setWindowTitle('eduBib')
        self.setGeometry(2000,200,500,182)
        self.setWindowIcon(QtGui.QIcon('eduBibLogo.png'))
        self.header = QtGui.QLabel(self)
        text = None
        self.header.setPixmap(QtGui.QPixmap(os.getcwd()+"/header2.png"))
        self.hwidth = 400
        self.hheight=157
        self.header.setGeometry(0,0,self.hwidth,self.hheight)
        self.inven=self.addbutton('Inventory',100,10,0,158))
        self.borrow =self.addbutton('Borrow',100,10,100,158)
        self.admin=self.addbutton('Administration',100,10,200,158)
        self.acqui=self.addbutton('Acquisition',100,10,300,158)
        self.quit=self.addbutton('Quit',100,10,400,158)
        self.quit.clicked.connect(self.quit_function)
        self.options = self.addbutton('Options',100,10,400,0)
        self.credits = self.addbutton('Credits',100,10,400,22)
        self.imprint = self.addbutton('Imprint',100,10,400,44)
        self.copyright = self.addbutton('Help',100,10,400,66)
        self.show()
  
    def addText(self,text):
        self.text = QtGui.QLabel(text,self)
        self.text.setFont(QtGui.QFont("Arial", 32))
        self.a = 500
        self.b= 600
        
        self.text.setGeometry(350,0,self.a,self.b)
    def addbutton(self,text,width,height,x,y):
        
        button = QtGui.QPushButton(text,self)
        button.move(x,y)
        button.resize(width,23)
        self.layout.addWidget(button)
        return button
    def quit_function(self):
        sys.exit()
def run():
    app = QtGui.QApplication(sys.argv)
 
    GUI = Window()
    sys.exit(app.exec_())
    
        
run()
