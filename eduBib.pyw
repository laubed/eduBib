"""
Main File
"""

from edubiblib.data.Database import database
from Tkinter import Tk

if __name__ == "__main__":
    """
    Main entry. Start the application here
    """
    tkFenster = Tk()
    tkFenster.title('eduBib - Hub')
    tkFenster.geometry('350x145')
    # Aktivierung des Fensters
    tkFenster.mainloop()