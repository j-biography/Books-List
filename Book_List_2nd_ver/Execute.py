

import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from Window_Main import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main = Window_Main()
    Main.show()
    sys.exit(app.exec())