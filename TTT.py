# Joshua Mazur
# Tic Tac Toe Project 2.

from Tkinter import * 
import turtle
import tkMessageBox

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
        frame.pack(side=RIGHT,fill=BOTH,expand=True)
	# Label in button frame
	self.label_message = StringVar()
	Label(buttonframe,textvariable=self.label_message).pack()
        # Rawturtle
        self.canvas = Canvas(frame,width=300,height=300,relief=SUNKEN)
        self.canvas.configure(background='blue')
        self.canvas.grid()
        self.canvas.pack(side=TOP,fill=BOTH,expand=True)
        self.turtle = turtle.RawTurtle(self.canvas) # embedded turtle.
        self.turtle.speed(10000)
        self.s = turtle.TurtleScreen(self.canvas) # Turtle's screen.
        # Setting up response to clicks.
        self.s.onclick(self.WhichSquare)
        # Draws initial grid.
        self.creategrid()
        # Initializes Game.
        self.g = game(self.turtle,self.label_message)

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
        if y > 50: 
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
        self.g.takeTurn(coor) # Begins the turn in game class.

##############################
'''The Game Class.'''

class game(TTT):
    """Contains all necessary variables and methods to play tictactoe alone."""

    def __init__(self,t,message_box):
        '''Initializes Instance Variables.'''
        self.board = [[".",".","."],[".",".","."],[".",".","."]] # creates an representation of an empty tictactoe board.
        self.turn = "X" # First turn is always starts with "X"
        self.numberofturns = 0 # In order to know when to end game in the case of a draw.
        self.turtle = t # The turtle used to draw the shapes.
        self.messages = message_box # Message box to give information. 
        self.gameover = False
        self.messages.set("Player: X")

    def newGame(self):
        '''Returns game to beginning.
        Pre: None
        Post: self.board and self.turn are reset.'''
        self.board = [[".",".","."],[".",".","."],[".",".","."]] # creates an representation of an empty tictactoe board.
        self.turn = "X" # First turn is always starts with "X"
        self.messages.set("Player: X")
        self.numberofturns = 0 # Resets turn accumulator.
        self.gameover = False
            
    def validMove(self,move):
        ''' Checks to see if an attempted move is possible.
        Pre: The move in question.
        Post: True or False answer depending on the Validity of the move.'''
        (y,x) = move
        answer = False
        if self.board[y][x] == ".":
            answer = True
        return answer

    def checkwin(self):
        """Checks all possibilities for a possible win.
        Pre: Uses self.board
        Post: Returns a list containing True or False in index one and winning 
        symbol if it applies in index two"""
        Answer = []
        # Horizontal Rows.
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]: # Top
            if self.board[0][0] != ".":
                Answer.append(True)
                Answer.append(self.board[0][0])
        elif self.board[1][0] == self.board[1][1] and self.board[1][1] ==self.board[1][2]: # Middle
            if self.board[1][0] != ".":
                Answer.append(True)
                Answer.append(self.board[1][0])
        elif self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]: # Bottom
            if self.board[2][0] != ".":
                Answer.append(True)
                Answer.append(self.board[2][0])
        # Vertical Column Possibilities
        elif self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]: # Left
            if self.board[0][0] != ".":
                Answer.append(True)
                Answer.append(self.board[0][0])
        elif self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]: # Middle
            if self.board[0][1] != ".":
                Answer.append(True)
                Answer.append(self.board[0][1])
        elif self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]: # Right
            if self.board[0][2] != ".":
                Answer.append(True)
                Answer.append(self.board[0][2])
        # Across Possibilites
        elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]: # Top
            if self.board[0][0] != ".":
                Answer.append(True)
                Answer.append(self.board[0][0])
        elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]: # Bottom
            if self.board[0][2] != ".":
                Answer.append(True)
                Answer.append(self.board[0][2])
        if len(Answer) == 0:
            Answer.append(False)
        return Answer

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

    def takeTurn(self,coor):
        '''Runs through steps to play tictactoe
        Pre: Players square choice in coor.
        Post: Changes self.turn to other players symbol.'''
        y = int(coor[0]) # Coordinates in term of x,y.
        x = int(coor[1])
        Variable = self.validMove((y,x)) # True or False Variable depeding on valid move.
        if self.gameover == False:
            if Variable == True:
                self.board[y][x] = self.turn # Placing piece on virtual board.
                self.drawshape(coor,self.turn) # Drawing shape on turtle canvas.
                Win = self.checkwin() # Checking for win.
                if self.turn == "X": # Changes turns.
                    self.turn = "O"
                else:
                    self.turn = "X"
                self.messages.set(str("Player: " + self.turn))
                if Win[0] == True: # If someone has won.
                    self.gameover = True
                    Message = str(Win[1]) + " wins!"
                    print(Message)
                    self.messages.set(Message)
                    tkMessageBox.showinfo("Winner", Message) # Winning Message is displayed.
                elif self.numberofturns == 8: 
                    self.messages.set("Cat")
                    tkMessageBox.showinfo("Tie", "Cat") # In case of Tie.
                else:
                    self.numberofturns += 1
            else:
                self.messages.set("Not a valid move.")
                tkMessageBox.showinfo("Invalid", "Not a valid Move") # If occupied spot is clicked.
                self.messages.set(str("Player: " + self.turn))
        else:
            Message = "The game is over, Hit New."
            print(Message)
            self.messages.set(Message)

root=Tk()
root.wm_title("Python Tic Tac Toe")
app=TTT(root)
root.mainloop() # creates window.
