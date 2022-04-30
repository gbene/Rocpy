



import sys
from PyQt5.QtWidgets import QApplication
from main import MainWindow

app = QApplication(sys.argv)
Rocpy = MainWindow()
Rocpy.show()
sys.exit(app.exec_())
