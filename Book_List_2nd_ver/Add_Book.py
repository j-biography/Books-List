
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtSql import *


class Add_Book(QMainWindow): 

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Library')
        self.setGeometry(500, 500, 500, 500)
        
        