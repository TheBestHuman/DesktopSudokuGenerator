import sys
from PySide.QtGui import *
from PySide.QtCore import *
from ui_mainWindow import *
from lib import build_sudoku_pdf

class MainWindow(QMainWindow, Ui_MainWindow):
   def __init__(self):
       super(MainWindow, self).__init__()
       self.setupUi(self)
       self.show()
   

if __name__ == '__main__':
   	build_sudoku_pdf.GeneratePDF(1, 1, 1, "Easy", False)

	app = QApplication(sys.argv)
	mainWin = MainWindow()
	ret = app.exec_()


	sys.exit( ret )
