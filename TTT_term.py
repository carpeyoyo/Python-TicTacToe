# Joshua Mazur
# This file is for testing the Tic Tac Toe game class by playing it in the terminal

from TTT_game import *
from TTT_AI import *

def board_numbers():
    # Prints out the board coordinates. 
    print "012"
    print "345"
    print "678"

def print_board(board):
    # Prints out the current board setting
    for i in range(0,3,1):
        string = ""
        for j in range(0,3,1):
            string += board[((i*3)+j)]
        print string

def main():
    board_numbers()
    g = game()
    a = AI()
    while g.gameover == False:
        # Beginning Output
        print(g.message)
        print_board(g.board)

        # Finding the move
        coor = int(raw_input("Please Enter Move: "))

        # Running through game move
        if coor < 9 and coor >= 0:
            if (g.TakeTurn(coor)):
                g.CheckEnd()
                if g.gameover == False: # Continue AI move if game is not over
                    ai_move = a.next_move(g.board)
                    if (g.TakeTurn(ai_move)): # Check move
                        g.CheckEnd() # Checking if AI made winning move or tie.
                    else:
                        error_message = "AI gave bad coordinate: " + str(ai_move)
                        exit()
        
    # End Message and goodbye        
    print(g.message)
    print(g.board)
    print("Goodbye")

main()
