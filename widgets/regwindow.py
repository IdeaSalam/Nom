from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from PyQt6.QtCore import *
import sys
import typing

class Regwindow(QMainWindow):
    def __init__(self,width = 1000, height = 600, tytle = "WIN") -> None:
        super().__init__() 
        
        self.setUpWindow()   
    def setUpWindow(self):
        
        # layy = QHBoxLayout()
        
        t_spl = QSplitter(Qt.Orientation.Horizontal)
        # self.log_edit = QLineEdit()
        # self.log_edit.setPlaceholderText("AAAAA")
        # layy.addWidget(self.log_in)
        # layy.addWidget(t_spl)
        # layy.addWidget(self.log_edit)
     
        self.lbl_name = QLabel("Ismingizni kiritng ")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Abdumalik")
        layout = QHBoxLayout()
        layout.addWidget(self.lbl_name)
        layout.addWidget(t_spl)
        layout.addWidget(self.name_edit)
        
        layot_em = QHBoxLayout()
        self.lbl_email = QLabel("Emailingizni kiriting ")
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("ism@gmail.com")
        layot_em.addWidget(self.lbl_email)
        layot_em.addWidget(t_spl)
        layot_em.addWidget(self.email_edit)
        
        layot_pas = QHBoxLayout()
        self.lbl_pass = QLabel("Parolingizni kiriting ")
        self.pass_edit = QLineEdit()
        self.pass_edit.setPlaceholderText("Prolingizni kiriting ")
        self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password)
        layot_pas.addWidget(self.lbl_pass)
        layot_pas.addWidget(t_spl)
        layot_pas.addWidget(self.pass_edit)
        
        lay_id = QHBoxLayout()
        self.lbl_tg = QLabel("Telegram ID")
        self.tid_edit = QLineEdit()
        self.tid_edit.setPlaceholderText("123434545")
        lay_id.addWidget(self.lbl_tg)
        lay_id.addWidget(t_spl)
        lay_id.addWidget(self.tid_edit)
        
        self.id_check = QCheckBox("Men telegram botdan ro'yxatdan o'tganman ")
        self.id_check.setChecked(False)
        
        
        v_lay = QVBoxLayout()
        self.log_in = QLabel("Ro'yxatdan o'tish oynasi",self)
        v_lay.addStretch(3)
        # v_lay.addWidget(layy)
        v_lay.addLayout(layout)
        v_lay.addLayout(layot_em)
        v_lay.addLayout(layot_pas)
        v_lay.addLayout(lay_id)
        v_lay.addLayout(layot_pas)
        v_lay.addWidget(self.id_check)
        
        center = QWidget()
        center.setLayout(v_lay)
        self.setCentralWidget(center)
        