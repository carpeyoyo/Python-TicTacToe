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
        self.x_offset = 0
        self.y_offset = 0
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
        # Adjusting values
        self.width = event.width
        self.height = event.height
        if self.width > self.height: # Keeping square
            self.x_offset = (self.width - self.height) / 2
            self.y_offset = 0
            self.width = self.height
        else:
            self.y_offset = (self.height - self.width) / 2
            self.x_offset = 0
            self.height = self.width
        # Redrawing 
        self.canvas.delete(ALL)
        self.creategrid()
        if (self.g.turn_number > 0):
            self.place_pieces()

    def creategrid(self):
        '''Draws the tictactow grid.
        Pre: uses class's canvas object.
        Post: draws lines on the canvas.'''
        ## Drawling Background
        self.canvas.create_rectangle(self.x_offset,self.y_offset,self.x_offset+self.width,self.y_offset+self.height,fill="grey")
        ## Drawling Lines
        length = self.width / 3
        # Line 1
        x0 = length + self.x_offset
        y0 = self.y_offset
        x1 = x0
        y1 = self.y_offset + self.height
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)
        # Line 2
        x0 = 2*length + self.x_offset
        y0 = self.y_offset
        x1 = x0
        y1 = self.y_offset + self.height
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)
        # Line 3
        x0 = self.x_offset
        y0 = self.y_offset + length
        x1 = self.x_offset + self.width
        y1 = y0
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)
        # Line 4
        x0 = self.x_offset
        y0 = self.y_offset + 2*length
        x1 = self.x_offset + self.width
        y1 = y0
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)

    def place_pieces(self):
        '''Draws the pieces on the board when necessary.
        Pre: Uses class's canvas and game objects.
        Post: Current pieces in game are are board. '''
        for i in range(0,9,1):
            piece = self.g.board[i]
            if piece != ".":
                self.drawshape(i,piece)

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
                self.label_message.set("Game Over, Hit New")

    def shape_coordinates(self,x,y):
        '''Finds the coordinates for either a circle or cross
        Pre: The center x,y as arguments, also uses current value of self.width.
        Post: The box coordinates are returned as a tuple.'''
        # Finding coordinates
        temp = self.width / 8 # half the length of a side
        x0 = x - temp
        y0 = y - temp
        x1 = x + temp
        y1 = y + temp
        return (x0,y0,x1,y1)

    def circle(self,x,y):
        '''Creates Circle on Board.
        Pre: Center of symbol.
        Post: Draws an O on the board at the center coordinate given.'''
        # Retrieving coordinates
        (x0,y0,x1,y1) = self.shape_coordinates(x,y)
        # Creating circle
        self.canvas.create_oval(x0,y0,x1,y1,outline="green",width=4.0)

    def cross(self,x,y):
        '''Creates Cross on board.
        Pre: Center is middle position of "X" on board.
        Post: Draws an X on the board at the center coordinate given'''
        # Retrieving coordinates
        (x0,y0,x1,y1) = self.shape_coordinates(x,y)
        # Creating lines
        self.canvas.create_line(x0,y0,x1,y1,fill="red",width=4.0)
        self.canvas.create_line(x0,y1,x1,y0,fill="red",width=4.0)

    def drawshape(self,coor,Turn):
        x = None
        y = None
        if coor == 0:            # Top Left
            x = self.width/6
            y = self.height/6
        elif coor == 1:          # Top Middle
            x = self.width/2
            y = self.height/6
        elif coor == 2:          # Top Right
            x = (5*self.width)/6
            y = self.height/6
        elif coor == 3:          # Middle Left
            x = self.width/6
            y = self.width/2         
        elif coor == 4:          # Center
            x = self.width/2
            y = self.width/2
        elif coor == 5:          # Middle Right
            x = (5*self.width)/6
            y = self.width/2
        elif coor == 6:          # Bottom Left
            x = self.width/6
            y = (5*self.width)/6
        elif coor == 7:          # Bottom Middle
            x = self.width/2
            y = (5*self.width)/6
        elif coor == 8:          # Bottom Right
            x = (5*self.width)/6
            y = (5*self.width)/6
            
        # Deciding Between Circle and square.
        if (x != None) and (y != None):
            x += self.x_offset
            y += self.y_offset
            if Turn == "O":      
                self.circle(x,y)
            else:
                self.cross(x,y)

