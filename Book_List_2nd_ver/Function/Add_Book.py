
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtSql import *

from UI.AddBook_UI import Ui_MainWindow


class Add_Book(QMainWindow, Ui_MainWindow): 

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        
        