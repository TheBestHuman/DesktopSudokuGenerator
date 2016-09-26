import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class Root(Widget):
	pass

class DesktopSudokuGenerator(App):
    title = 'Desktop Sudoku Generator'
    
    def build(self):
    	return Root()
        

if __name__ == '__main__':
    DesktopSudokuGenerator().run()
