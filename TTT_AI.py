# Joshua Mazur
# AI class

import random

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
        # Method for choosing the best next move based on going through possible next steps
        # Pre: The list of coordinates left to choose, the current board state as a nine
        #      character list, and the current piece to be played.
        # Post: Returns the coordinate choosen.

        # Placeholder
        return self.easy_next_move(leftlist)
        

    ## Common methods
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
