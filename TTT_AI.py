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

    def next_move(self, currentboard):
        # Returns the next move the AI wished to make on the board
        # Pre: Current board setup as a 9 character list
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
            answer = self.medium_next_move(leftlist,currentboard)
        else: # hard
            answer = self.hard_next_move(leftlist,currentboard)

        # Returning answer
        return answer

    def easy_next_move(self,leftlist):
        # Method for randomly choosing next easy move
        # Pre: List of coordinates that are still open
        # Post: Returns coordinate randomly chosen
        index = random.randrange(0,len(leftlist),1)
        return leftlist[index]

    def medium_next_move(self,leftlist,currentboard):
        # Method for choosing random move, unless there is a move open to win.
        # Pre: The list of coordinates left to choose, and the current board state
        #      as a nine character list
        # Post: Returns the coordinate chosen. 
        
        # Placeholder
        return self.easy_next_move(leftlist)

    def hard_next_move(self,leftlist,currentboard):
        # Method for choosing the best next move based on going through possible next steps
        # Pre: The list of coordinates left to choose, and the current board state as a
        #      nine character list
        # Post: Returns the coordinate choosen.

        # Placeholder
        return self.easy_next_move(leftlist)
        
