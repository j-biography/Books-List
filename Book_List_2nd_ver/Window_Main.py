
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtSql import *

from UI.Main_UI import Main_UI
from Add_Book import Add_Book


class Window_Main(QMainWindow, Main_UI): 

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Book List')
 
        self.Add_Book_Window = Add_Book()
        
        
        self.pushButton_2.clicked.connect(self.Add_Book_Window.show)