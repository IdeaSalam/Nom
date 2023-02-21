from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class SignSignal(QObject):
    sings = pyqtSignal()
class SignWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.set_ui()
        self.up = SignSignal()

    def set_ui(self, width = 700, height = 500, title = "Однокласснеки") -> None:
        super().__init__()
        qw = QIcon("image/ok.png")
        self.setWindowIcon(qw)
        self.setWindowTitle(title)
        self.setGeometry(700, 200, width, height)
        
        self.kirish = QLabel("Вход",self)
        self.kirish.setObjectName("main")
        self.kirish.setStyleSheet("#main{font-size:24px}")
        self.kirish.setGeometry(width//2-60, height//2-230, 150, 30)
        
        self.lbl = QLabel("Телефон или адрес эл. почты",self)
        self.lbl.setObjectName("main1")
        self.lbl.setStyleSheet("#main1{font-size:18px}")
        self.lbl.setGeometry(width//2-180, height//2-170, 350, 30)
        self.lin = QLineEdit(self)
        self.lin.setGeometry(width//2-180, height//2-140, 350, 30)
        
        self.lbl1 = QLabel("Пароль",self)
        self.lbl1.setObjectName("main2")
        self.lbl1.setStyleSheet("#main2{font-size:18px}")
        self.lbl1.setGeometry(width//2-180, height//2-90, 350, 30)
        self.lin1 = QLineEdit(self)
        self.lin1.setGeometry(width//2-180, height//2-60, 350, 30)
        
        self.btn = QPushButton("Войты в Однокласснеки",self)
        self.btn.setGeometry(width//2-180, height//2-10, 350, 35)
        
        self.btn1 = QPushButton("Войты по QR-коду",self)
        self.btn1.setGeometry(width//2-180, height//2+45, 350, 35) 
        
        self.lbl2 = QLabel("не получается войти?",self)
        self.lbl2.setObjectName("main5")
        self.lbl2.setStyleSheet("#main5{font-size:16px}")
        self.lbl2.setGeometry(width//2-85, height//2+95, 170, 35)
        
        self.lbl2 = QLabel("------------Нет профиля в Одноклассниках--------------",self)
        self.lbl2.setObjectName("main5")
        self.lbl2.setStyleSheet("#main5{font-size:16px}")
        self.lbl2.setGeometry(width//2-190, height//2+135, 400, 35)
        
        icon = QIcon("image/vk.png")
        icon1 = QIcon("image/search.png")
        icon2 = QIcon("image/apple.png")
        icon3 = QIcon("image/yandex.png")
        
        self.icon = QPushButton(icon,"",self)
        self.icon1 = QPushButton(icon1,"",self)
        self.icon2 = QPushButton(icon2,"",self)
        self.icon3 = QPushButton(icon3,"",self)
        
        self.icon.setGeometry(width//2-150, height//2+185, 50, 50)
        self.icon1.setGeometry(width//2-70, height//2+185, 50, 50)
        self.icon2.setGeometry(width//2+10, height//2+185, 50, 50)
        self.icon3.setGeometry(width//2+90, height//2+185, 50, 50)
        
        
        style = """
        QPushButton{
            background-color:orange;
            border-radius: 16px;
            font-size:18px;
        }
        QPushButton::hover{
            border:1px solid white;
            color:black;
            border-radius:16px;
        }
        """
        style1 = """
        QLineEdit{
            border-radius: 16px;
            font-size:18px;
        }
        QLineEdit::hover{
            border:1px solid white;
            color:black;
            border-radius:16px;
        }
        """
        
        self.btn.setStyleSheet(style)
        self.btn1.setStyleSheet(style)
        
        self.lin.setStyleSheet(style1)
        self.lin1.setStyleSheet(style1)
        
        self.btn1.clicked.connect(self.clic_regbtn)
        
    def clic_regbtn(self):
        self.up.sings.emit()
        self.hide()
        