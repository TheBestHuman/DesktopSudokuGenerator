import sys
from PySide.QtGui import *
from PySide.QtCore import *
from ui_mainWindow import *
from lib import build_sudoku_pdf
import time
import os

#Inherit from QThread
class SudokuWorker(QtCore.QThread):

	total_puzzles = 1
	puzzles_per_page = 1
	pages_per_pdf = 1
	difficulty = 'Easy' 
	include_solutions = True 
	outputdirectory = "."
	
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
		build_sudoku_pdf.GeneratePDF(self, self.total_puzzles, self.puzzles_per_page, self.pages_per_pdf, self.difficulty, self.include_solutions)
		
	def killmesignal(self):
		build_sudoku_pdf.stop = True

	def reallykillme(self):
		self.quit()

class MainWindow(QMainWindow, Ui_MainWindow):

	startTime = time.time()
	progressIncrement = 0.0
	running = False
	timeLeft = 0
	killself = False


	def __init__(self):
		super(MainWindow, self).__init__()

		self.sudoku_worker = SudokuWorker()
		self.sudoku_worker.updateProgress.connect(self.setProgress)

		self.setupUi(self)

		self.go_button.clicked.connect(self.Go)


		self.progressBar.setValue(0)
		self.progress_label.setText("")



		self.show()     

	def setControls(self, enabled):

		self.go_button.setEnabled(enabled)
		self.include_solutions.setEnabled(enabled)
		self.difficulty.setEnabled(enabled)
		self.puzzles_per_page.setEnabled(enabled)
		self.num_puzzles.setEnabled(enabled)

	def Go(self):
		#self.progressBar.show()
		self.progressBar.setValue(0)
		self.progress_label.setText("Beginning file generation process.")
		#self.progress_label.show()

		#set PDF generation parameters
		self.sudoku_worker.total_puzzles = int(self.num_puzzles.toPlainText())

		self.progressIncrement = float(100.0/float(self.num_puzzles.toPlainText()))

		self.sudoku_worker.puzzles_per_page = (int(self.puzzles_per_page.currentText()))
		self.sudoku_worker.difficulty = self.difficulty.currentText()
		self.sudoku_worker.include_solutions = self.include_solutions.isChecked()
		#start the clock
		startTime = time.time()
		progressIncrement = 0
		self.running = True
		self.setControls(False)
		#run PDF generation on a separate thread
		self.sudoku_worker.start()

	def setProgress(self, progress):

		if(progress > 10 and self.running == True):
			
			previousProgress = self.progressBar.value()
			#print "previous progress:" + str(previousProgress)
			if(progress > previousProgress):
				elapsedTime = float(time.time() - self.startTime)
				self.timeLeft = float(100-progress) * float(elapsedTime / progress)
				#print elapsedTime


			self.progress_label.setText(str(progress) + "% complete." )
			#" Estimated time remaining: " + str(int(self.timeLeft / 60)).zfill(2) + ":" + str(int(self.timeLeft % 60)).zfill(2))
		elif progress > 0:
			self.progress_label.setText(str(progress) + "% complete." )
			#Calculating time remaining...")
		if progress == 100:
			self.running = False
			self.progress_label.setText("File generation complete.")
			progress = 0
			self.setControls(True)
			if(self.killself):
				print "quitting"
				QCoreApplication.quit()

		self.progressBar.setValue(progress)


	def closeEvent(self, event):
		if(self.running and self.killself == False):
			#if a process is running, tell it to save and quit
			#print "killme signal"
			self.sudoku_worker.killmesignal()
			#print "setting killself"
			self.killself = True
			self.progress_label.setText("Saving, please wait");
			event.ignore()
		else:
			self.sudoku_worker.reallykillme()
			event.accept() # let the window close
			# do stuff
			#if can_exit:
			#else:
			#   event.ignore()


if __name__ == '__main__':
	build_sudoku_pdf.freezemultiprocessingsupport()

	app = QApplication(sys.argv)
	mainWin = MainWindow()
	ret = app.exec_()


	sys.exit( ret )
