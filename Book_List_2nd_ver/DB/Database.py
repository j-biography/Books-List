

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtSql import *


def createDB():
   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('Book_DB.db')
	
   if not db.open():
      QMessageBox.critical(None, QApplication.tr("Cannot open database"),
         QMessageBox.Cancel)
			
      return False
		
   query = QSqlQuery()
   
   
   query.exec("create table Book(Author , Book_Name)")
   query.exec("insert into Book values(?, ?)")
   
   query.addBindValue()
   query.addBindValue()
   
   query.exec()

   return True
	
if __name__ == '__main__':
   import sys
	
   app = QApplication(sys.argv)
   createDB()
