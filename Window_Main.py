
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import sys
from Window_Function import *


class Window_Main(QMainWindow): # QMainWindow는 최상위 위젯이며, 자동으로 QWidget이 하위 자식으로 생성됨.

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): 
        widget = QWidget()
        grid = QGridLayout(widget)
        grid.setAlignment(Qt.AlignCenter)
        
        grid.addWidget(QLabel('Library'), 0, 0)
        grid.addWidget(QPushButton('Add Book'), 1, 0)
        grid.addWidget(QLineEdit(), 2, 0)
        grid.addWidget(QPushButton('Search'), 2, 1)
        grid.setColumnStretch(1, 1)
        
        self.setCentralWidget(widget)
        self.setWindowTitle('Library')
        self.setGeometry(500, 500, 500, 500)
        self.setLayout(grid)





# class Window_Main(QDialog):

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Library')
#         self.setGeometry(1000, 1000, 400, 400)

#         self.Add_Book_Button = QPushButton('Add')
#         self.Add_Book_Button.clicked.connect(self.show_new)

#         main_layout = QVBoxLayout()
#         main_layout.addWidget(self.Add_Book_Button)
#         self.setLayout(main_layout)
    
#     def show_new(self):
#         self.w = Add_Book()
#         self.w.show()

    
# class Add_Book(QWidget):

#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel('New_Window')
#         layout.addWidget(self.label)
#         self.setLayout(layout) 
    
