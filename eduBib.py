"""
Main File
"""

from PyQt4 import QtGui

import sys
from edubiblib.data.Database import database
import Tkinter

if __name__ == "__main__":
    """
    Main entry. Start the application here
    """
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hello World!")
    b.move(50, 20)
    w.setWindowTitle("eduBib Splash")
    w.show()
    sys.exit(app.exec_())