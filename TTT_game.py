# Joshua Mazur

##############################
'''The Game Class.'''

class game:
    """Contains all necessary variables and methods to play tictactoe alone."""

    def __init__(self):
        # Game Constructor
        # New game method is called
        self.newGame()

    def newGame(self):
        # Sets game variables to default
        # Creates default board, turn, number of turns, gameover state, message, and winner
        self.board = [".",".",".",".",".",".",".",".","."]
        self.turn = "X"
        self.turn_number = 0
        self.message = "Player X to move."
        self.gameover = False
        self.end_symbol = -1

    def CheckEnd(self):
	    # Checks if game is over
	    # Pre: Uses self.board and self.turn_number to decide if game is over
        # Post: sets self.gameover to True is game is over, and sets self.message to end message

        if self.turn_number > 4: # No reason to check otherwise
        
            # Checking those involving top left square
            if self.board[0] != ".":
                if (self.board[0] == self.board[1]) and (self.board[1] == self.board[2]): # Across Top
                    self.gameover = True
                    self.message = self.board[0] + " Wins!"
                    self.end_symbol = 0
                if (self.board[0] == self.board[3]) and (self.board[3] == self.board[6]): # Down Left
                    self.gameover = True
                    self.message = self.board[0] + " Wins!"
                    self.end_symbol = 1
                if (self.board[0] == self.board[4]) and (self.board[4] == self.board[8]): # Diagonal from top left
                    self.gameover = True
                    self.message = self.board[0] + " Wins!"
                    self.end_symbol = 2
            # Checking those involving top right square
            if self.board[2] != ".":
                if (self.board[2] == self.board[4]) and (self.board[4] == self.board[6]): # Diagonal from bottom left
                    self.gameover = True
                    self.message = self.board[2] + " Wins!"
                    self.end_symbol = 3
                if (self.board[2] == self.board[5]) and (self.board[5] == self.board[8]): # Down right
                    self.gameover = True
                    self.message = self.board[2] + " Wins!"
                    self.end_symbol = 4
            # Checking those involving bottom middle square
            if self.board[7] != ".":
                if (self.board[7] == self.board[6]) and (self.board[6] == self.board[8]): # Across Bottom
                    self.gameover = True
                    self.message = self.board[7] + " Wins!"
                    self.end_symbol = 5
                if (self.board[7] == self.board[1]) and (self.board[1] == self.board[4]): # Down middle
                    self.gameover = True
                    self.message = self.board[7] + " Wins!"
                    self.end_symbol = 6
            # Checking across middle
            if self.board[3] != ".":
                if (self.board[3] == self.board[4]) and (self.board[4] == self.board[5]): # Across middle
                    self.gameover = True
                    self.message = self.board[3] + " Wins!"
                    self.end_symbol = 7
            # Checking if tie
            if self.gameover == False:
                if self.turn_number > 8:
                    self.gameover = True
                    self.message = "Tie"
    
    def ValidMove(self,coor):
        # Finds if move is valid
        # Pre: Uses self.board and the coor following the board numbers that can be found in board_numbers
        # Post: Returns true if move can be made, false otherwise
        answer = False
        if self.board[coor] == ".":
            answer = True
        return answer

    def TakeTurn(self,coor):
        # Makes move if possible
        # Pre: Uses self.board and input coordinate
        # Post: Returns true if move was made
        answer = False
        if self.gameover == False:
            answer = self.ValidMove(coor)
            if answer == True: 
                # Piece can be placed
                self.board[coor] = self.turn
                self.turn_number += 1
                # Switching Pieces
                if self.turn == "X":
                    self.turn = "O"
                else:
                    self.turn = "X"
                # Creating message
                self.message = "Player " + self.turn + " to move"
            else:
                # Creating message for invalid move
                self.message = "Invalid move. Player " + self.turn + " to move"
        return answer
