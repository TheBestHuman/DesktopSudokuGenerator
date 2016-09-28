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

def GeneratePDF(total_puzzles, puzzles_per_page, pages_per_pdf, difficulty, include_solutions, outputdirectory = "."):

    output_filename = "Sudoku_" + difficulty + "_" + time.strftime("%Y%m%d-%H%M%S") + ".pdf"
    doc = canvas.Canvas(filename=output_filename, pagesize=defaultPageSize)

    g = sudoku_maker.SudokuGenerator()
    j = 0
    puzzlelist = []
    while (j <  total_puzzles):
    	puzzles = g.make_unique_puzzles(1)
    	#print puzzles[0][1].value_string()
    	if(puzzles[0][1].value_string() == difficulty):
    		puzzlelist = puzzlelist + puzzles
    		j = j + 1
    i = 1
    for puz, d in puzzlelist:

        generatePage(puz,d, doc, i)
        doc.showPage()

        i = i + 1
    doc.save()
     #   fd, outfile = tempfile.mkstemp(dir=os.path.join(DATA_DIR, d.value_string()))
     #   print outfile
     #   out = os.fdopen(fd, 'w')
     #   pickle.dump(puz, out)
     #   out.close()
