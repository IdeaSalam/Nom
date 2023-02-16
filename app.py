from widgets.regwindow import *
from PyQt6.QtWidgets import *
import sys
if __name__=="__main__":
    app = QApplication(sys.argv)
    win = Regwindow(width=300,height=300)
    win.show()
    app.exec()
    
    