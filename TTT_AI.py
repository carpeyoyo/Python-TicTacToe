# Joshua Mazur
# AI class

import random
from copy import deepcopy
import TTT_game

class AI:
    def __init__(self,level):
        # Current time seed for random calls
        random.seed()
        # Setting difficulty level
        if (level == 0) or (level == 1):
            self.difficulty = level # 0 for easy, 1 for medium, 2 for hard
        elif (level == 2):
            self.difficulty = level
            self.hard_method = self.hard_next_move()
        else:
            errormessage = "Error setting difficulty in AI constructor.\nDifficulty given: " + str(level) + ". Needs to be either 0, 1, or 2."
            print(errormessage)
            exit()

    def next_move(self, currentboard, currentpiece):
        # Returns the next move the AI wished to make on the board
        # Pre: Current board setup as a 9 character list, and the currentpiece
        # Post: Returns AI's coordinate choice
        
        # List of coordinates that are left in play
        leftlist = [] 
        for i in range(0,len(currentboard),1): 
            if currentboard[i] == ".":
                leftlist.append(i)
                
        # Finding move
        if self.difficulty == 0: # Easy
            answer = self.easy_next_move(leftlist)
        elif self.difficulty == 1: # Medium
            answer = self.medium_next_move(leftlist,currentboard,currentpiece)
        else: # hard
            self.leftlist = leftlist
            self.currentboard = currentboard
            self.currentpiece = currentpiece
            answer = self.hard_method.next()

        # Returning answer
        return answer

    def easy_next_move(self,leftlist):
        # Method for randomly choosing next easy move
        # Pre: List of coordinates that are still open
        # Post: Returns coordinate randomly chosen
        index = random.randrange(0,len(leftlist),1)
        return leftlist[index]

    def medium_next_move(self,leftlist,currentboard,currentpiece):
        # Method for choosing random move, unless there is a move open to win.
        # Pre: The list of coordinates left to choose, and the current board state
        #      as a nine character list
        # Post: Returns the coordinate chosen. 

        if len(leftlist) <= 5: # Minimum number of moves for a winning move to exist
            # Checking if win is possible in next move
            winlist = self.win_next(leftlist,currentboard,currentpiece)
            if len(winlist) > 1: # More than one winning move
                index = random.randrange(0,len(winlist),1)
                answer = winlist[index] # Randomly choose one
            elif len(winlist) == 1: # One winning move
                answer = winlist[0]
            else: # Currently no winning moves
                answer = self.easy_next_move(leftlist)
        else: # Minimum number of moves not yet reached
            answer = self.easy_next_move(leftlist)

        return answer

    def hard_next_move(self):
        # Method for choosing a move based on strategy
        # Pre: The list of coordinates left to choose, the current board state as a nine
        #      character list, and the current piece to be played.
        # Post: Returns the coordinate choosen.

        # Variable setup
        favor_list = [0,2,4,6,8] # Favor corners and center
        opponentpiece = "X"
        if self.currentpiece == "X":
            opponentpiece = "O"

        # AI went first
        if len(self.leftlist) == 9: 
            ## First Move (randomly choose from favor list
            index = random.randrange(0,len(favor_list),1)
            answer = favor_list[index]
            yield answer
            # Need to fill in rest

        # Other Player went first    
        else:
            ## First Move
            if self.currentboard[4] == ".": # Claim center if empty
                yield 4
                havecenter = True
            else: # Choose randomly of corners left
                favor_left = list(set(favor_list) & set(self.leftlist))
                index = random.randrange(0,len(favor_left),1)
                lastmove = answer = favor_left[index]
                yield answer
                havecenter = False

            ## Second Move
            answer = self.check_block(self.leftlist,self.currentboard,opponentpiece)
            if answer != -1: # Need to block
                yield answer
            else: # Did not need to block
                if havecenter: # Need to check for tricks
                    # Corner Trick
                    answer = self.check_corner_trick(self.leftlist,self.currentboard,opponentpiece)
                    if answer != -1:
                        yield answer
                    else:
                        # Split Trick
                        answer = self.check_split_trick(self.currentboard,opponentpiece)
                        if answer != -1:
                            yield answer
                        else:
                            # L Trick
                            answer = self.check_L_trick(self.currentboard,opponentpiece)
                            if answer != -1:
                                yield answer
                            else:
                                print("AI: Choosing randomly.")
                                yield self.easy_next_move(self.leftlist)
                else:
                    # Checking bluff trick
                    answer = self.check_bluff_trick(self.currentboard,lastmove,opponentpiece)
                    if answer != -1:
                        yield answer
                    else:
                        print("AI: Choosing randomly.")
                        yield self.easy_next_move(self.leftlist)

        ## Rest
        while True:
            answer = self.check_win_block(self.leftlist,self.currentboard,self.currentpiece,opponentpiece)
            if answer != -1:
                yield answer
            else:
                print("AI: Choosing Randomly.")
                yield self.easy_next_move(self.leftlist)
                
    # hard_next_move support methods
    def check_bluff_trick(self,currentboard,lastmove,opponentpiece): 
        # Checking whether opponent is trying to bluff using center
        ####### Should only be called on the second move for an AI that went second
        # Pre: The current board as a nine character list, the coordinate of the AI's last move, and
        #      the opponent's piece symbol
        # Post: Returns coordinate if trick is discovered, -1 otherwise
        answer = -1
        trick = False
        if (lastmove == 0) and (currentboard[4] == opponentpiece) and (currentboard[8] == opponentpiece):
            trick = True
            choicelist = [2,6]
        elif (lastmove == 2) and (currentboard[4] == opponentpiece) and (currentboard[6] == opponentpiece):
            trick = True
            choicelist = [0,8]
        elif (lastmove == 8) and (currentboard[4] == opponentpiece) and (currentboard[0] == opponentpiece):
            trick = True
            choicelist = [2,6]
        elif (lastmove == 6) and (currentboard[4] == opponentpiece) and (currentboard[2] == opponentpiece):
            trick = True
            choicelist = [0,8]
        if trick:
            print("AI: Assuming bluff trick.")
            index = random.randrange(0,2,1)
            answer = choicelist[index]
        return answer
    
    def check_L_trick(self,currentboard,opponentpiece):
        # Checks to see if opponent is trying L trick
        # Pre: The currentboard as a nine character list, and the opponent's piece symobl
        # Post: Returns coordinate needed to block, -1 otherwise
        answer = -1
        if (currentboard[1] == opponentpiece) and (currentboard[3] == opponentpiece):
            if currentboard[0] == ".":
                answer = 0
        if (currentboard[1] == opponentpiece) and (currentboard[5] == opponentpiece):
            if currentboard[2] == ".":
                answer = 2
        if (currentboard[3] == opponentpiece) and (currentboard[7] == opponentpiece):
            if currentboard[6] == ".":
                answer = 6
        if (currentboard[5] == opponentpiece) and (currentboard[7] == opponentpiece):
            if currentboard[8] == ".":
                answer = 8
        if answer != -1:
            print("AI: Assuming L trick.")
        return answer
    
    def check_split_trick(self,currentboard,opponentpiece):
        # Checks if opponent if trying "split" trick
        # Pre: Currentboard board a nine character list, and opponent's piece symbol
        # Post: Returns move if opponent is trying split trick, -1 otherwise
        answer = -1
        if (currentboard[1] == opponentpiece) and (currentboard[8] == opponentpiece):
            if currentboard[2] == ".":
                answer = 2
        if (currentboard[1] == opponentpiece) and (currentboard[6] == opponentpiece):
            if currentboard[0] == ".":
                answer = 0
        if (currentboard[5] == opponentpiece) and (currentboard[6] == opponentpiece):
            if currentboard[8] == ".":
                answer = 8
        if (currentboard[5] == opponentpiece) and (currentboard[0] == opponentpiece):
            if currentboard[2] == ".":
                answer = 2
        if (currentboard[2] == opponentpiece) and (currentboard[7] == opponentpiece):
            if currentboard[8] == ".":
                answer = 8
        if (currentboard[0] == opponentpiece) and (currentboard[7] == opponentpiece):
            if currentboard[6] == ".":
                answer = 6
        if (currentboard[2] == opponentpiece) and (currentboard[3] == opponentpiece):
            if currentboard[0] == ".":
                answer = 0
        if (currentboard[3] == opponentpiece) and (currentboard[8] == opponentpiece):
            if currentboard[6] == ".":
                answer = 6
        if answer != -1:
            print("AI: Assuming Split trick")
        return answer
    
    def check_corner_trick(self,leftlist,currentboard,opponentpiece):
        # Returns coordinate if opponent is trying to use the corner trick
        # Pre: currentboard and the opponent's piece symbol
        # Post: Returns coordinate if opponent is trying trick, -1 otherwise
        answer = -1
        trick = False
        if (currentboard[0] == opponentpiece) and (currentboard[8] == opponentpiece):
            trick = True
        elif (currentboard[2] == opponentpiece) and (currentboard[6] == opponentpiece):
            trick = True
        if trick:
            favor_left = list(set([1,3,5,7]) & set(leftlist))
            index = random.randrange(0,len(favor_left),1)
            answer = favor_left[index]
            print("AI: Assuming corner trick.")
        return answer
    
    def check_win_block(self,leftlist,currentboard,currentpiece,opponentpiece):
        # Finds whether a win is possible in the next move, or if a block will be necessary
        # Pre: The leftlist of avaliable moves, the currentboard as a nine character list, and the current
        #      player's piece.
        # Post: Returns the coordinate for a win or a block if either exists, or -1
        # Checking if a win is possible in the next move
        winlist = self.win_next(leftlist,currentboard,currentpiece)
        if len(winlist) > 0: # Winning move is avaliable
            index = random.randrange(0,len(winlist),1)
            answer = winlist[index]
            print("AI: I can win.")
        else:
            answer = self.check_block(leftlist,currentboard,opponentpiece)
        return answer

    def check_block(self,leftlist,currentboard,opponentpiece):
        # Finds whether a block will be necessary on this move
        # Pre: The leftlist of avaliable moves, the currentboard as a nine character list, and the current
        #      player's piece.
        # Post: Returns coordinate that needs blocked, -1 otherwise.
        answer = -1
        # Checking if a block is needed
        loselist = self.win_next(leftlist,currentboard,opponentpiece)
        # Need to block
        if len(loselist) > 0:
            index = random.randrange(0,len(loselist),1)
            answer = loselist[index]
            print("AI: I need to block.")
        return answer
                
    # Common Method
    def win_next(self,leftlist,currentboard,currentpiece):
        # Returns list of coordinates for leftlist that will allow the currentpiece to win after the next move
        # Pre: The list of coordinates left to choose, the currentboard setup as a nine character list, and
        #      the current piece to be played.
        answerlist = []

        for coor in leftlist:
            if coor == 0:
                if (currentboard[1] == currentpiece) and (currentboard[2] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[3] == currentpiece) and (currentboard[6] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[4] == currentpiece) and (currentboard[8] == currentpiece):
                    answerlist.append(coor)
            elif coor == 1:
                if (currentboard[0] == currentpiece) and (currentboard[2] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[4] == currentpiece) and (currentboard[7] == currentpiece):
                    answerlist.append(coor)
            elif coor == 2:
                if (currentboard[0] == currentpiece) and (currentboard[1] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[4] == currentpiece) and (currentboard[6] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[5] == currentpiece) and (currentboard[8] == currentpiece):
                    answerlist.append(coor)
            elif coor == 3:
                if (currentboard[0] == currentpiece) and (currentboard[6] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[4] == currentpiece) and (currentboard[5] == currentpiece):
                    answerlist.append(coor)
            elif coor == 4:
                if (currentboard[0] == currentpiece) and (currentboard[8] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[1] == currentpiece) and (currentboard[7] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[2] == currentpiece) and (currentboard[6] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[3] == currentpiece) and (currentboard[5] == currentpiece):
                    answerlist.append(coor)
            elif coor == 5:
                if (currentboard[3] == currentpiece) and (currentboard[4] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[2] == currentpiece) and (currentboard[8] == currentpiece):
                    answerlist.append(coor)
            elif coor == 6:
                if (currentboard[0] == currentpiece) and (currentboard[3] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[2] == currentpiece) and (currentboard[4] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[7] == currentpiece) and (currentboard[8] == currentpiece):
                    answerlist.append(coor)
            elif coor == 7:
                if (currentboard[1] == currentpiece) and (currentboard[4] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[6] == currentpiece) and (currentboard[8] == currentpiece):
                    answerlist.append(coor)
            elif coor == 8:
                if (currentboard[0] == currentpiece) and (currentboard[4] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[2] == currentpiece) and (currentboard[5] == currentpiece):
                    answerlist.append(coor)
                elif (currentboard[6] == currentpiece) and (currentboard[7] == currentpiece):
                    answerlist.append(coor)

        return answerlist
