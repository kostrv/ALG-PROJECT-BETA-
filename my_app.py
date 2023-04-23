from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (    
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QListWidget, QLineEdit, QMainWindow) 

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        '''Окно, в котором располагается приветствие'''
        super().__init__()
        #создаем и настраиваем графические элементы:
        self.initUI()

        #устанавливает связи между элементами
        self.connects()
        
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        #старт:
        self.show()

    def initUI(self):
        '''создает графические элементы'''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)


    def next_click(self):
        self.tw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    
    '''установка вида окна (надпись, размер, место)'''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
app = QApplication([])
mw = MainWin()
app.exec_()