import sudoku_maker
from defaults import *
import pickle
import os
import tempfile
import sys
import sudoku_maker
import sudoku
from reportlab.lib.units import inch
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.pdfgen import canvas
import sys
import random
from defaults import *
import os
import pickle
import time
import math
import threading
import random

PAGE_WIDTH, PAGE_HEIGHT=defaultPageSize


styles = getSampleStyleSheet()

ParaStyle = styles["Normal"]

def renderPuzzle(page, puzzle, top, left, size, fontSize=24, thinLine=1, thickLine=4):
	right = left + size
	bottom = top - size
	page.saveState()

	box_height = size / 9
	for i in range(0, 10):
		if i in [0, 3, 6, 9]:
			page.setLineWidth(thickLine)
		else:
			page.setLineWidth(thinLine)
		page.line(left, top - i * box_height, right, top - i * box_height)
		page.line(left + i * box_height, top, left + i * box_height, bottom)

	s = puzzle.to_string()
	nums = s.split()
	#print puzzle
	page.setFont('Times-Bold',fontSize)
	for row in range(0, 9):
		for col in range(0, 9):
			num = nums[row * 9 + col]
			if num != '0':
				page.drawString(left + col * box_height + box_height * 0.38, top - row * box_height - box_height * 0.65, num)
	page.restoreState()

def generatePage(puzzle, dpuz, page, puzzlenum, difficulty='Any', showFooter=True):

	puz = puzzle
	d = dpuz

	top = PAGE_HEIGHT
	left = 36
	renderPuzzle(page, puz, top - 72 * 2, left, PAGE_WIDTH - 72, fontSize=24)

	page.setFont('Times-Bold',12)
	page.drawString(left, top - 72 * 1.5, "Puzzle %d (%s, difficulty rating %.02f)" % (puzzlenum, d.value_string(), d.value))
	#if showFooter:
	#    generateFooter(page)
	#return puz, d
def generateFourUpPage(puzzles, page, puzzlenum, difficulty='Any'):

    inch = 72
    top = PAGE_HEIGHT
    left = 36
    size = (PAGE_WIDTH - inch * 1.5) / 2
    coords = [
        (top - inch * 1, left),
        (top - inch * 1, left + size + inch * .5),
        (top - inch * 1 - size - inch, left),
        (top - inch * 1 - size - inch, left + size + inch * .5),
    ]

    i = 0
    for puzzle in puzzles:
        puz, d = puzzle
        renderPuzzle(page, puz, coords[i][0], coords[i][1], size, fontSize=16)
        page.setFont('Times-Bold',12)
        page.drawString(coords[i][1], coords[i][0] + inch * 0.25, "Puzzle %d (%s, difficulty rating %.02f)" % (puzzlenum + i, d.value_string(), d.value))
        i += 1

    return puz, d

def generateSolutions(page, puzzles):
    col = row = 0
    i = 0
    for puz, d in puzzles:
        i += 1
        page.setFont('Times-Bold',8)
        page.drawString(36 + col * 72 * 2.5, PAGE_HEIGHT - 72 - row * 72 * 2.5 + 6, "Puzzle %d (%s, difficulty rating %.02f)" % (i, d.value_string(), d.value))
        solver = sudoku.SudokuRater(puz.grid,verbose=False, group_size=puz.group_size)
        solver.solve()
        renderPuzzle(page, solver, PAGE_HEIGHT - 72 - row * 72 * 2.5, 36 + col * 72 * 2.5, 72 * 2, fontSize=10, thickLine=2)
        col += 1
        if col == 3:
            col = 0
            row += 1
            if row == 4:
                col = row = 0
                page.showPage()

def GeneratePDF(progress, total_puzzles, puzzles_per_page, pages_per_pdf, difficulty, include_solutions, outputdirectory = "."):

	progress.updateProgress.emit(0)
	progress_increment = 100/total_puzzles
	current_progress = 0

	output_filename = "Sudoku_" + difficulty + "_" + time.strftime("%Y%m%d-%H%M%S") + ".pdf"
	doc = canvas.Canvas(filename=output_filename, pagesize=defaultPageSize)

	g = sudoku_maker.SudokuGenerator()
	j = 0
	puzzlelist = []
	while (j <  total_puzzles):
		g = sudoku_maker.SudokuGenerator()
		puzzles = g.make_unique_puzzles(1)

		print "[" + puzzles[0][1].value_string() + "] [" + difficulty + "]"
		if puzzles[0][1].value_string() == difficulty or difficulty == 'Random'  :
			puzzlelist = puzzlelist + puzzles
			j = j + 1
			current_progress = current_progress + progress_increment
			progress.updateProgress.emit(current_progress)
	i = 1

	if puzzles_per_page == 4:
		currentpagelist = []
		for puz, d in puzzlelist:

			currentpagelist.append((puz,d))
			if(i%4 == 0):
				generateFourUpPage(currentpagelist, doc, i - (len(currentpagelist)-1))
				doc.showPage()
				currentpagelist = []

			i = i + 1

		generateFourUpPage(currentpagelist, doc, i - (len(currentpagelist)))
		doc.showPage()
	else:
		for puz, d in puzzlelist:

			generatePage(puz,d, doc, i)
			doc.showPage()

			i = i + 1

	if include_solutions:
		generateSolutions(doc, puzzlelist)
		doc.showPage()

	doc.save()

	progress.updateProgress.emit(100)
