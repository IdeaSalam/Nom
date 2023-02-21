from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Log_in(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.set_ui()
    def set_ui(self,width = 800, height = 200, title = "Log In"):
        
        self.setGeometry(width, height, 600, 400)
        self.setWindowTitle(title)
        split = QSplitter(Qt.Orientation.Horizontal)
        self.lay1 = QVBoxLayout()
        self.lbl1 = QLabel("Ismingizni kiriting",self)
        self.lin1 = QLineEdit()
        self.lin1.setPlaceholderText("Example")
        self.lay1.addWidget(self.lbl1)
        # self.lay.addWidget(split)
        self.lay1.addWidget(self.lin1)
        
        self.lay2 = QVBoxLayout()
        self.lbl2 = QLabel("Ismingizni kiriting",self)
        self.lin2 = QLineEdit()
        self.lin2.setPlaceholderText("Example")
        self.lay2.addWidget(self.lbl2)
        # self.lay.addWidget(split)
        self.lay2.addWidget(self.lin2)
        
        self.lay3 = QVBoxLayout()
        self.lbl3 = QLabel("Ismingizni kiriting",self)
        self.lin3 = QLineEdit()
        self.lin3.setPlaceholderText("Example")
        self.lay3.addWidget(self.lbl3)
        # self.lay.addWidget(split)
        self.lay3.addWidget(self.lin3)
        
        v_lay = QVBoxLayout()
        v_lay.addLayout(self.lay1)
        v_lay.addLayout(self.lay2)
        v_lay.addLayout(self.lay3)
        
        center = QWidget()
        center.setLayout(v_lay)
        self.setCentralWidget(center)
        
        
        
        