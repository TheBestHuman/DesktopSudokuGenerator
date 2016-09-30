# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Sep 29 20:16:41 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 338)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 2)
        self.num_puzzles = QtGui.QTextEdit(self.centralWidget)
        self.num_puzzles.setEnabled(True)
        self.num_puzzles.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num_puzzles.setFont(font)
        self.num_puzzles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.num_puzzles.setObjectName("num_puzzles")
        self.gridLayout.addWidget(self.num_puzzles, 0, 1, 1, 1)
        self.puzzles_per_page = QtGui.QComboBox(self.centralWidget)
        self.puzzles_per_page.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.puzzles_per_page.setFont(font)
        self.puzzles_per_page.setObjectName("puzzles_per_page")
        self.puzzles_per_page.addItem("")
        self.puzzles_per_page.addItem("")
        self.gridLayout.addWidget(self.puzzles_per_page, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.go_button = QtGui.QPushButton(self.centralWidget)
        self.go_button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.go_button.setFont(font)
        self.go_button.setObjectName("go_button")
        self.gridLayout.addWidget(self.go_button, 4, 1, 1, 1)
        self.include_solutions = QtGui.QCheckBox(self.centralWidget)
        self.include_solutions.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.include_solutions.setFont(font)
        self.include_solutions.setText("")
        self.include_solutions.setObjectName("include_solutions")
        self.gridLayout.addWidget(self.include_solutions, 3, 1, 1, 1)
        self.progress_label = QtGui.QLabel(self.centralWidget)
        self.progress_label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progress_label.setFont(font)
        self.progress_label.setObjectName("progress_label")
        self.gridLayout.addWidget(self.progress_label, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.difficulty = QtGui.QComboBox(self.centralWidget)
        self.difficulty.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.difficulty.setFont(font)
        self.difficulty.setObjectName("difficulty")
        self.difficulty.addItem("")
        self.difficulty.addItem("")
        self.difficulty.addItem("")
        self.difficulty.addItem("")
        self.difficulty.addItem("")
        self.gridLayout.addWidget(self.difficulty, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Difficulty:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Number of puzzles:", None, QtGui.QApplication.UnicodeUTF8))
        self.num_puzzles.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.puzzles_per_page.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.puzzles_per_page.setItemText(1, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Include Solutions", None, QtGui.QApplication.UnicodeUTF8))
        self.go_button.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_label.setText(QtGui.QApplication.translate("MainWindow", "Include Solutions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Puzzles per page:", None, QtGui.QApplication.UnicodeUTF8))
        self.difficulty.setItemText(0, QtGui.QApplication.translate("MainWindow", "Random", None, QtGui.QApplication.UnicodeUTF8))
        self.difficulty.setItemText(1, QtGui.QApplication.translate("MainWindow", "Easy", None, QtGui.QApplication.UnicodeUTF8))
        self.difficulty.setItemText(2, QtGui.QApplication.translate("MainWindow", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.difficulty.setItemText(3, QtGui.QApplication.translate("MainWindow", "Hard", None, QtGui.QApplication.UnicodeUTF8))
        self.difficulty.setItemText(4, QtGui.QApplication.translate("MainWindow", "Very Hard", None, QtGui.QApplication.UnicodeUTF8))

