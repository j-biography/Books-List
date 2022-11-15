
import sys
from PySide6.QtSql import QSqlDatabase, QSqlQuery


Database = QSqlDatabase.addDatabase("QSQLITE")
Database.setDatabaseName("Book_Database")



if not Database.open():
    print("Unable to connect to the database")
    sys.exit(1)