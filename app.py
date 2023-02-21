from widgets.regwindow import *
from PyQt6.QtWidgets import *
from widgets.signWin import *
from widgets.signal import Log_in
import sys
if __name__=="__main__":
    app = QApplication(sys.argv)
    win = Regwindow() 
    rg = SignWindow()
    rg.show()
    rg.up.sings.connect(win.show)
    # wi = Log_in()
    # wi.show()
    
    app.exec()
    
    