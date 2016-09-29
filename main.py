import sys
from PySide.QtGui import *
from PySide.QtCore import *
from ui_mainWindow import *
from lib import build_sudoku_pdf

#Inherit from QThread
class SudokuWorker(QtCore.QThread):

    #This is the signal that will be emitted during the processing.
    #By including int as an argument, it lets the signal know to expect
    #an integer argument when emitting.
    updateProgress = QtCore.Signal(int)

    #You can do any extra things in this init you need, but for this example
    #nothing else needs to be done expect call the super's init
    def __init__(self):
        QtCore.QThread.__init__(self)

    #A QThread is run by calling it's start() function, which calls this run()
    #function in it's own "thread". 
    def run(self):
        build_sudoku_pdf.GeneratePDF(self, 5, 4, 1, "Easy", False)
        self.updateProgress.emit(1)



class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()

		self.sudoku_worker = SudokuWorker()
		self.sudoku_worker.updateProgress.connect(self.setProgress)

		self.setupUi(self)

		self.go_button.clicked.connect(self.Go)
		self.progressBar.hide()
		self.progressBar.setValue(0);
		self.progress_label.hide()

		self.show()     
	
	def Go(self):
		self.progressBar.show()
		self.progressBar.setValue(0)
		self.progress_label.setText("Beginning file generation process.")
		self.progress_label.show()
		self.sudoku_worker.start()

	def setProgress(self, progress):
		self.progressBar.setValue(progress)
		if progress == 100:
			self.progressBar.hide()
			self.progress_label.setText("File generation complete.")




if __name__ == '__main__':
   	

	app = QApplication(sys.argv)
	mainWin = MainWindow()
	ret = app.exec_()


	sys.exit( ret )
