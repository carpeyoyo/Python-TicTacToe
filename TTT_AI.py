import random

class AI:
    def __init__(self):
        random.seed()

    def next_move(self, currentboard):
        leftlist = []
        for i in range(0,len(currentboard),1):         
            if currentboard[i] == ".":
                leftlist.append(i)
        index = random.randrange(0,len(leftlist),1)
        return leftlist[index]
