# Joshua Mazur
# AI class

import random
from copy import deepcopy
import TTT_game

class AI_stats:
    def __init__(self):
        self.coordinate = -1
        self.win = 0
        self.lost = 0
        self.tie = 0
        self.reached_bottom = False

class AI:
    def __init__(self,level):
        # Current time seed for random calls
        random.seed()
        # Setting difficulty level
        if (level == 0) or (level == 1) or (level == 2):
            self.difficulty = level # 0 for easy, 1 for medium, 2 for hard
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
            answer = self.hard_next_move(leftlist,currentboard,currentpiece)

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

    def hard_next_move(self,leftlist,currentboard,currentpiece):
        # Method for choosing a move based on strategy
        # Pre: The list of coordinates left to choose, the current board state as a nine
        #      character list, and the current piece to be played.
        # Post: Returns the coordinate choosen.

        continue_on = True
        favor_list = [0,2,4,6,8] # Favor corners and center

        # If AI is making first move, favor certain positions and choose randomly
        if len(leftlist) == 9: # No previous moves have been made
            index = random.randrange(0,5,1)
            answer = favor_list[index]
            continue_on = False

        # If enough moves have been made to check for win or lose
        elif len(leftlist) <= 6:
            # Checking if a win is possible in the next move
            winlist = self.win_next(leftlist,currentboard,currentpiece)
            if len(winlist) > 0: # Winning move is avaliable
                index = random.randrange(0,len(winlist),1)
                answer = winlist[index]
                continue_on = False
                print("AI: I can win.")
            else:
                # Checking if a block is needed
                if currentpiece == "X":
                    nextpiece = "O"
                else:
                    nextpiece = "X"
                loselist = self.win_next(leftlist,currentboard,nextpiece)
                # Need to block
                if len(loselist) > 0:
                    index = random.randrange(0,len(loselist),1)
                    answer = loselist[index]
                    continue_on = False
                    print("AI: I need to block.")

        # If move has not yet been found
        if continue_on:
            if len(leftlist) == 8: # Favoring corners and center again
                if currentboard[4] == ".":  # Claim center
                    answer = 4
                else: # Else choose an open corner
                    movelist = []
                    for coor in favor_list:
                        if currentboard[coor] == ".":
                            movelist.append(coor)
                    index = random.randrange(0,len(movelist),1)
                    answer = movelist[index]
            else:
                # Finding opponent's piece
                opponentpiece = "X"
                if currentpiece == "X":
                    opponentpiece = "O"
                # Checking if opponent is using corner trick
                trick = False
                if (currentboard[0] == opponentpiece) and (currentboard[8] == opponentpiece):
                    trick = True
                elif (currentboard[2] == opponentpiece) and (currentboard[6] == opponentpiece):
                    trick = True
                # If it was a trick
                if trick:
                    print("AI: Assuming corner trick.")
                    choice_list = list(set([1,3,5,7]) & set(leftlist))
                    index = random.randrange(0,len(choice_list),1)
                    answer = choice_list[index]
                # Else continue on
                else:
                    # Checking for split tricks
                    trick = False
                    if (currentboard[1] == opponentpiece) and (currentboard[8] == opponentpiece):
                        if currentboard[2] == ".":
                            answer = 2
                            trick = True
                    if (currentboard[1] == opponentpiece) and (currentboard[6] == opponentpiece):
                        if currentboard[0] == ".":
                            answer = 0
                            trick = True
                    if (currentboard[5] == opponentpiece) and (currentboard[6] == opponentpiece):
                        if currentboard[8] == ".":
                            answer = 8
                            trick = True
                    if (currentboard[5] == opponentpiece) and (currentboard[0] == opponentpiece):
                        if currentboard[2] == ".":
                            answer = 2
                            trick = True
                    if (currentboard[2] == opponentpiece) and (currentboard[7] == opponentpiece):
                        if currentboard[8] == ".":
                            answer = 8
                            trick = True
                    if (currentboard[0] == opponentpiece) and (currentboard[7] == opponentpiece):
                        if currentboard[6] == ".":
                            answer = 6
                            trick = True
                    if (currentboard[2] == opponentpiece) and (currentboard[3] == opponentpiece):
                        if currentboard[0] == ".":
                            answer = 0
                            trick = True
                    if (currentboard[3] == opponentpiece) and (currentboard[8] == opponentpiece):
                        if currentboard[6] == ".":
                            answer = 6
                            trick = True
                    if trick:
                        print("AI: Assuming split trick.")
                    # Else choose randomly
                    else:
                        print("AI: Made it to random.")
                        answer = self.easy_next_move(leftlist)
                            
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
