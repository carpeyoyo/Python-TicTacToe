# Joshua Mazur
# Creation of window

from Tkinter import * 
import turtle
import tkMessageBox
from TTT_game import *
from TTT_gui import *

root=Tk()
root.wm_title("Python Tic Tac Toe")
app=TTT(root)
root.mainloop() # creates window.
