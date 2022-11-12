
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtSql import *

from Main_UI import *


class Window_Main(QMainWindow, Main_UI): 

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Book List')


    def Add_book(q, Title, Date_of_Purchase, Author):
        q.addBindValue(Title)
        q.addBindValue(Date_of_Purchase)
        q.addBindValue(Author)