# Joshua Mazur
# This file is for testing the Tic Tac Toe game class by playing it in the terminal

import TTT_game
import TTT_AI

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
    g = TTT_game.game()

    # Asking for AI game difficulity
    difficulty_message = "Enter game difficulity (0 for easy, 1 for medium, 2 for hard): "
    difficulty = int(raw_input(difficulty_message))
    a = TTT_AI.AI(difficulty)

    # Game main loop
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
                    ai_move = a.next_move(g.board,g.turn)
                    if (g.TakeTurn(ai_move)): # Check move
                        g.CheckEnd() # Checking if AI made winning move or tie.
                    else:
                        error_message = "AI gave bad coordinate: " + str(ai_move)
                        exit()
        
    # End Message and goodbye
    print("\n"+g.message)
    print_board(g.board)
    print("Goodbye")

main()
