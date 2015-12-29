# Joshua Mazur
# This file is for testing the Tic Tac Toe game class by playing it in the terminal

from TTT_game import *

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
        
    # End Message and goodbye        
    print(g.message)
    print("Goodbye")

main()
