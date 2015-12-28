# Joshua Mazur

##############################
'''The Game Class.'''

class game:
    """Contains all necessary variables and methods to play tictactoe alone."""

    def __init__(self):
        '''Initializes Instance Variables.'''
        self.board = [[".",".","."],[".",".","."],[".",".","."]] # creates an representation of an empty tictactoe board.
        self.turn = "X" # First turn is always starts with "X"
        self.numberofturns = 0 # In order to know when to end game in the case of a draw.
        self.gameover = False
	self.message = ""
	self.shape = ""

    def newGame(self):
        '''Returns game to beginning.
        Pre: None
        Post: self.board and self.turn are reset.'''
        self.board = [[".",".","."],[".",".","."],[".",".","."]] # creates an representation of an empty tictactoe board.
        self.turn = "X" # First turn is always starts with "X"
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

    def takeTurn(self,coor):
        '''Runs through steps to play tictactoe
        Pre: Players square choice in coor.
        Post: Changes self.turn to other players symbol.'''
        if coor != "out":
            y = int(coor[0]) # Coordinates in term of x,y.
            x = int(coor[1])
            Variable = self.validMove((y,x)) # True or False Variable depeding on valid move.
            if self.gameover == False:
                if Variable == True:
                    self.board[y][x] = self.turn # Placing piece on virtual board.
                    Win = self.checkwin() # Checking for win.
                    if self.turn == "X": # Changes turns.
                        self.turn = "O"
                    else:
                        self.turn = "X"
                    if Win[0] == True: # If someone has won.
                        self.gameover = True
                        Message = str(Win[1]) + " wins!"
                        print(Message)
                        print("Winner", Message) # Winning Message is displayed.
                    elif self.numberofturns == 8: 
                        print("Tie", "Cat") # In case of Tie.
                    else:
                        self.numberofturns += 1
                else:
                    self.message = "Not a valid Move. " + self.turn + " to move." # If occupied spot is clicked.
            else:
                Message = "The game is over, Hit New."
                print(Message)

