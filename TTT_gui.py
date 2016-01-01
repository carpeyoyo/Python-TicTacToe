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
        # Canvas for drawing
        self.width = 400
        self.height = 400
        self.canvas = Canvas(frame,width=self.width,height=self.height,relief=SUNKEN)
        self.canvas.grid()
        self.canvas.pack(side=TOP,fill=BOTH,expand=True)
        # Setting event responses
        self.canvas.bind("<Configure>",self.draw_board)
        self.canvas.bind("<Button-1>",self.WhichSquare)
        # Initializes Game.
        self.g = game()
        self.label_message.set(self.g.message)

    def new(self):
        '''Creates new game.
        Pre: None
        Post: resets the turtle, draws new grid, and initiates new grid class.'''
        self.label_message.set("")
        self.canvas.delete("all")
        self.g.newGame()
        self.creategrid()
        self.label_message.set(self.g.message)

    def draw_board(self,event):
        '''Draws the tic tac toe board.
        Pre: The event passed to the widget, when board needs redrawn.
        Post: Board is drawn on window.'''
        self.width = event.width
        self.height = event.height
        if self.width > self.height:
            self.width = self.height
        else:
            self.height = self.width
        self.canvas.delete(ALL)
        self.creategrid()

    def creategrid(self):
        '''Draws the tictactow grid.
        Pre: uses class's canvas object.
        Post: draws lines on the canvas.'''
        ## Drawling Background
        self.canvas.create_rectangle(0,0,self.width,self.height,fill="grey")
        ## Drawling Lines
        # Line 1
        self.canvas.create_line(self.width/3,0,self.width/3,self.height,width=4.0)
        # Line 2
        self.canvas.create_line(2*self.width/3,0,2*self.width/3,self.height,width=4.0)
        # Line 3
        self.canvas.create_line(0,self.height/3,self.width,self.height/3,width=4.0)
        # Line 4
        self.canvas.create_line(0,2*self.height/3,self.width,2*self.height/3,width=4.0)

    def WhichSquare(self,event):
        '''Determines which square has been clicked.
        Pre: x and y are the coordinates of the click.
        Post: initiates the takeTurn method from game class.'''
        ## Checking which square was clicked

        # Initial values
        x = event.x
        y = event.y
        coor = "out"
        first_x = self.width/3
        second_x = (2*self.width)/3
        third_x = self.width
        first_y = self.height/3
        second_y = (2*self.height)/3
        third_y = self.height

        # Determing square by coordinates
        if (x > 0) and (y > 0):
            if y < first_y:
                if x < first_x:
                    coor = 0 # Top left square.
                elif x < second_x:
                    coor =  1 # Top middle square.
                elif x < third_x:
                    coor = 2 # Top Right square.
            elif y < second_y:
                if x < first_x:
                    coor = 3 # Middle left square.
                elif x < second_x:
                    coor = 4 # Center Square.
                elif x < third_x:
                    coor = 5 # Middle rigth square.
            elif y < third_y:
                if x < first_x:
                    coor = 6 # Bottom left square.
                elif x < second_x:
                    coor = 7 # Bottom Middle square.
                elif x < third_x:
                    coor = 8 # Bottom Right Square.
        print str(x) + "," + str(y)
        print "Coordinate: " + str(coor)
        # Entering move in game
        '''
        if coor != "out":
            if self.g.gameover == False:
                current_sym = self.g.turn
                if (self.g.TakeTurn(coor)): # Begins the turn in game class.
                    self.drawshape(coor,current_sym) # Draws shape if valid move
                    self.g.CheckEnd() # Checks to see if game is over
                    self.label_message.set(self.g.message)
                else: # Invalid Move
                    self.label_message.set(self.g.message)
            else:
                self.label_message.set("The game is over. Start a new game.")
        '''

    def circle(self,center):
        '''Creates Circle on Board.
        Pre: Center of symbol.
        Post: Draws an O on the board at the center coordinate given.'''
        (x,y) = center
        pass

    def cross(self,center):
        '''Creates Cross on board.
        Pre: Center is middle position of "X" on board.
        Post: Draws an X on the board at the center coordinate given'''
        (x,y) = center
        pass

    def drawshape(self,coor,Turn):
        if coor == 0:            # Top Left
            center = (-100,100)
        elif coor == 1:          # Top Middle
            center = (0,100)
        elif coor == 2:          # Top Right
            center = (100,100)
        elif coor == 3:          # Middle Left
            center = (-100,0)
        elif coor == 4:          # Center
            center = (0,0)
        elif coor == 5:          # Middle Right
            center = (100,0)
        elif coor == 6:          # Bottom Left
            center = (-100,-100)
        elif coor == 7:          # Bottom Middle
            center = (0,-100)
        elif coor == 8:          # Bottom Right
            center = (100,-100)
        if Turn == "O":             # Deciding Between Circle and square.
            self.circle(center)
        else:
            self.cross(center)

