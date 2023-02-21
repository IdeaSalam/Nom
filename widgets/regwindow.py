from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from PyQt6.QtCore import *
import sys
import typing

class Regwindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__() 
        self.setUpWindow() 
        self.can_btn.clicked.connect(QApplication.quit) 
        self.send_btn.clicked.connect(self.send_click) 
        # self.setGeometry(700, 200, width, height)
    def setUpWindow(self,width = 700, height = 400, tytle = "WIN"):
        
        self.setGeometry(700, 200, width, height)
        self.lbl_name = QLabel("Ismingizni kiritng")
        self.name_edit = QLineEdit()
        t_spl = QSplitter(Qt.Orientation.Horizontal)
        self.name_edit.setPlaceholderText("Abdumalik")
        layout = QHBoxLayout()
        layout.addWidget(self.lbl_name)
        layout.addWidget(t_spl)
        layout.addWidget(self.name_edit)
        
        self.layout2 = QHBoxLayout()
        self.tel_btn = QLabel("Telefon raqamingizni kiriting ")
        self.tel_edit = QLineEdit()
        self.tel_edit.setPlaceholderText("press Ctrl+X")
        self.layout2.addWidget(self.tel_btn)
        self.layout2.addWidget(t_spl)
        self.layout2.addWidget(self.tel_edit)
        
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
        
        self.send_btn = QPushButton("Ro'yxatdan o'tish")
        self.can_btn = QPushButton("Bekor qilish")
        style = """
        QPushButton{
            background-color: green;
            border-radius: 2px;
        }
        QPushButton::hover{
            border:1px solid white;
            color:black;
            border-radius:5px;
        }
        """
        self.send_btn.setStyleSheet(style)
        self.can_btn.setStyleSheet(style)
        self.btn_lay = QHBoxLayout()
        self.btn_lay.addWidget(self.send_btn)
        self.btn_lay.addWidget(self.can_btn)
                
        v_lay = QVBoxLayout()
        v_lay.addLayout(layout)
        v_lay.addLayout(layot_em)
        v_lay.addLayout(self.layout2)
        v_lay.addLayout(layot_pas)
        v_lay.addLayout(lay_id)
        v_lay.addLayout(layot_pas)
        v_lay.addWidget(self.id_check)
        v_lay.addLayout(self.btn_lay)
        
        center = QWidget()
        center.setLayout(v_lay)
        self.setCentralWidget(center)
    def check_data(self):
        td = self.tid_edit
        return len(td.text())==9 and td.text().isdigit()
    def send_click(self):
        if self.check_data():
            pass
        else:
            QMessageBox.critical(self,"Xatolik","Telegram ID bunday bo'lishi mumkin emas!!!")
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_1.value:
            self.close()
        elif a0.key() == Qt.Key.Key_2.value:
            self.name_edit.setText("Abdumalik")
        elif a0.key() == Qt.Key.Key_H.value:
            self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password)
        elif a0.key() == Qt.Key.Key_Q.value:
            self.pass_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif a0.key() == Qt.Key.Key_D.value:
            self.pass_edit.setInputMask("*")
        elif a0.key() == Qt.Key.Key_X.value:
            self.tel_edit.setInputMask("+(\9\98)99-999-99-99")
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.setWindowTitle("Mouse double clicked")
    # def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
    #     x = a0.position().x()
    #     y = a0.position().y()
    #     self.lbl_name.setText("x="+str(x)+";"+"y="+str(y))