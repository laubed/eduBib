"""
Main File
"""
from PIL import ImageTk, Image
import Tkinter as tk


if __name__ == "__main__":
    """
    Main entry. Start the application here
    """
    def loadAll():
        import edubiblib
        root.destroy()

    root = tk.Tk()
    root.overrideredirect(1)
    img = ImageTk.PhotoImage(Image.open("misc/splash.png"))
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    root.after(50, loadAll)
    root.mainloop()

