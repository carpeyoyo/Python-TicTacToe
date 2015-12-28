# Joshua Mazur

from Tkinter import * 
import turtle
from TTT_game import *

#####################
"""The Class to Create an App."""

class TTT(object):
    def __init__(self, master):
        ''' Initializes the variables for the game and tkinter window.
        Pre: The Tkinter master is supplied.
        Post: Game and window initialized. '''
        self.turn = "O"
        # Adding menu bar
        self.themenu = Menu(master)
        self.file_label_menu = Menu(self.themenu, tearoff=0)
        self.file_label_menu.add_command(label="New",command = self.new)
        self.file_label_menu.add_separator()
        self.file_label_menu.add_command(label="Exit",command=master.quit)
        self.themenu.add_cascade(label="File",menu=self.file_label_menu)
        master.config(menu=self.themenu)
        # Frames used in window.
        buttonframe = Frame(master)
        buttonframe.pack()
        frame = Frame(master)
        frame.pack(side=TOP,fill=BOTH,expand=True)
	# Label in button frame
	self.label_message = StringVar()
	Label(buttonframe,textvariable=self.label_message,font=("serif",18)).pack()
        # Rawturtle
        self.canvas = Canvas(frame,width=400,height=400,relief=SUNKEN)
        self.canvas.grid()
        #self.canvas.pack(side=TOP,fill=BOTH,expand=True)
        self.canvas.pack(side=TOP)
        self.turtle = turtle.RawTurtle(self.canvas) # embedded turtle.
        self.turtle.speed(10000)
        self.s = turtle.TurtleScreen(self.canvas) # Turtle's screen.
        # Setting up initial center of board
        self.x_center = 0
        self.y_center = 0
        self.maximum = 400
        # Setting up response to clicks.
        self.s.onclick(self.WhichSquare)
        # Draws initial grid.
        self.creategrid()
        # Initializes Game.
        self.g = game()

    def new(self):
        '''Creates new game.
        Pre: None
        Post: resets the turtle, draws new grid, and initiates new grid class.'''
        self.canvas.delete("all")
        self.turtle.reset()
        self.turtle.speed(10000)
        self.creategrid()
        self.g.newGame()

    def creategrid(self):
        '''Draws the tictactow grid.
        Pre: uses class's turtle object.
        Post: draws lines on the turtle canvas by means of overlapping rectangles.'''
        self.turtle.up()
        self.turtle.goto(-150,150)
        self.turtle.down()
        self.turtle.fillcolor("gray")
        self.turtle.begin_fill()
        self.turtle.goto(-150,-150)
        self.turtle.goto(150,-150)
        self.turtle.goto(150,150)
        self.turtle.goto(-150,150)
        self.turtle.end_fill()
        self.turtle.up()
        self.turtle.goto(-150,50) # First Line
        self.turtle.down()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.end_fill()
        self.turtle.up()
        self.turtle.goto(-150,-50) # Second Line
        self.turtle.down()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.end_fill()
        self.turtle.up()
        self.turtle.goto(-50,150) # Third Line
        self.turtle.down()
        self.turtle.right(90)
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.end_fill()
        self.turtle.up()
        self.turtle.goto(50,150) # Forth Line
        self.turtle.down()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.forward(300)
        self.turtle.left(90)
        self.turtle.forward(2)
        self.turtle.left(90)
        self.turtle.end_fill()
        self.turtle.up()

    def WhichSquare(self,x,y):
        '''Determines which square has been clicked.
        Pre: x and y are the coordinates of the click.
        Post: initiates the takeTurn method from game class.'''
        print str(x) + "," + str(y)
        if (x > 150) or (x < -150) or (y > 150) or (y < -150):
            coor = "out" # If click was out of bounds.
        elif y > 50: 
            if x < -50:
                coor = "00" # Top left square.
            elif x < 50:
                coor = "01" # Top middle square.
            elif x < 150:
                coor = "02" # Top Right square.
        elif y > -50:
            if x < -50:
                coor = "10" # Middle left square.
            elif x < 50:
                coor = "11" # Center Square.
            elif x < 150:
                coor = "12" # Middle rigth square.
        elif y > -150:
            if x < -50:
                coor = "20" # Bottom left square.
            elif x < 50:
                coor = "21" # Bottom Middle square.
            elif x < 150:
                coor = "22" # Bottom Right Square.
        print coor
        self.g.takeTurn(coor) # Begins the turn in game class.

    def circle(self,center):
        '''Creates Circle on Board.
        Pre: Center of symbol.
        Post: Draws an O on the board at the center coordinate given.'''
        (x,y) = center
        y_1 = y-25
        y_2 = y-20
        self.turtle.setheading(0)
        self.turtle.up()
        self.turtle.fillcolor("black")
        self.turtle.goto(x,y_1)
        self.turtle.begin_fill()
        self.turtle.circle(25)
        self.turtle.goto(x,y_2)
        self.turtle.circle(20)
        self.turtle.end_fill()

    def cross(self,center):
        '''Creates Cross on board.
        Pre: Center is middle position of "X" on board.
        Post: Draws an X on the board at the center coordinate given'''
        (x,y) = center
        x_1 = x - 25
        x1 = x - 20
        y_1 = y + 25
        x_2 = x + 25
        x2 = x + 20
        y_2 = y - 25
        self.turtle.goto((x_1,y_1))
        self.turtle.up()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.goto((x_1,y_1))
        self.turtle.down()
        self.turtle.goto((x1,y_1))
        self.turtle.goto((x_2,y_2))
        self.turtle.goto((x2,y_2))
        self.turtle.goto((x_1,y_1))
        self.turtle.end_fill()
        self.turtle.up()
        self.turtle.goto((x_1,y_2))
        self.turtle.begin_fill()
        self.turtle.down()
        self.turtle.goto((x1,y_2))
        self.turtle.goto((x_2,y_1))
        self.turtle.goto((x2,y_1))
        self.turtle.goto((x_1,y_2))
        self.turtle.end_fill()
        self.turtle.up()

    def drawshape(self,coor,Turn):
        if coor == "00":            # Top Left
            center = (-100,100)
        elif coor == "01":          # Top Middle
            center = (0,100)
        elif coor == "02":          # Top Right
            center = (100,100)
        elif coor == "10":          # Middle Left
            center = (-100,0)
        elif coor == "11":          # Center
            center = (0,0)
        elif coor == "12":          # Middle Right
            center = (100,0)
        elif coor == "20":          # Bottom Left
            center = (-100,-100)
        elif coor == "21":          # Bottom Middle
            center = (0,-100)
        elif coor == "22":          # Bottom Right
            center = (100,-100)
        if Turn == "O":             # Deciding Between Circle and square.
            self.circle(center)
        else:
            self.cross(center)

