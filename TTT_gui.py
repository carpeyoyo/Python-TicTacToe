# Joshua Mazur
# GUI class

from Tkinter import * 
import TTT_game
import TTT_AI

#####################
"""The Class to Create an App."""

class TTT(object):
    def __init__(self, master):
        ''' Initializes the variables for the game and tkinter window.
        Pre: The Tkinter master is supplied.
        Post: Game and window initialized. '''
        self.turn = "O"
        ## Adding menu bar
        self.themenu = Menu(master)
        self.file_label_menu = Menu(self.themenu, tearoff=0)
        # Submenu
        self.file_new_submenu = Menu(self.file_label_menu)
        self.file_new_submenu.add_command(label="Human vs. Human",command = self.new_human)
        # Difficulty submenus
        self.new_submenu_ai_first_submenu = Menu(self.file_new_submenu)
        self.new_submenu_ai_first_submenu.add_command(label="Easy",command = self.new_ai_first_easy)
        self.new_submenu_ai_first_submenu.add_command(label="Medium",command = self.new_ai_first_medium)
        self.new_submenu_ai_first_submenu.add_command(label="Hard",command = self.new_ai_first_hard)
        self.file_new_submenu.add_cascade(label="Computer vs. Human",menu=self.new_submenu_ai_first_submenu)
        self.new_submenu_ai_submenu = Menu(self.file_new_submenu)
        self.new_submenu_ai_submenu.add_command(label="Easy",command=self.new_ai_easy)
        self.new_submenu_ai_submenu.add_command(label="Medium",command=self.new_ai_medium)
        self.new_submenu_ai_submenu.add_command(label="Hard",command=self.new_ai_hard)
        self.file_new_submenu.add_cascade(label="Human vs Computer",menu=self.new_submenu_ai_submenu)
        self.file_label_menu.add_cascade(label="New Game",menu=self.file_new_submenu)
        self.file_label_menu.add_separator()
        self.file_label_menu.add_command(label="Exit",command=master.quit)
        self.themenu.add_cascade(label="File",menu=self.file_label_menu)
        master.config(menu=self.themenu)
        # Frames used in window.
        buttonframe = Frame(master)
        buttonframe.pack()
        frame = Frame(master)
        frame.pack(side=TOP,fill=BOTH,expand=True)
        # Label in button frame
        self.label_message = StringVar()
        Label(buttonframe,textvariable=self.label_message,font=("serif",16)).pack()
        # Canvas for drawing
        self.width = 400
        self.height = 400
        self.x_offset = 0
        self.y_offset = 0
        self.canvas = Canvas(frame,width=self.width,height=self.height,relief=SUNKEN)
        self.canvas.grid()
        self.canvas.pack(side=TOP,fill=BOTH,expand=True)
        # Setting event responses
        self.canvas.bind("<Configure>",self.draw_board)
        self.canvas.bind("<Button-1>",self.WhichSquare)
        # Initializes Game.
        self.g = TTT_game.game()
        self.label_message.set(self.g.message)
        # AI is false
        self.use_ai = False

    # AI Button wrapper functions
    def new_ai_first_easy(self):
        self.new_ai_first(0)

    def new_ai_first_medium(self):
        self.new_ai_first(1)

    def new_ai_first_hard(self):
        self.new_ai_first(2)

    def new_ai_easy(self):
        self.new_ai(0)

    def new_ai_medium(self):
        self.new_ai(1)

    def new_ai_hard(self):
        self.new_ai(2)

    def new_ai_first(self,difficulty):
        self.new_ai(difficulty)
        ai_move = self.a.next_move(self.g.board,self.g.turn)
        self.g.TakeTurn(ai_move)
        self.drawshape(ai_move,"X")
        self.label_message.set(self.g.message)

    def new_ai(self,difficulty):
        self.new()
        self.use_ai = True
        self.a = TTT_AI.AI(difficulty)

    def new_human(self):
        self.new();
        self.use_ai = False

    def new(self):
        '''Creates new game.
        Pre: None
        Post: Draws new grid, and initiates new grid class.'''
        self.label_message.set("")
        self.canvas.delete("all")
        self.g.newGame()
        self.creategrid()
        self.label_message.set(self.g.message)

    def draw_board(self,event):
        '''Draws the tic tac toe board.
        Pre: The event passed to the widget, when board needs redrawn.
        Post: Board is drawn on window.'''
        # Adjusting values
        self.width = event.width
        self.height = event.height
        if self.width > self.height: # Keeping square
            self.x_offset = (self.width - self.height) / 2
            self.y_offset = 0
            self.width = self.height
        else:
            self.y_offset = (self.height - self.width) / 2
            self.x_offset = 0
            self.height = self.width
        # Redrawing 
        self.canvas.delete(ALL)
        self.creategrid()
        if (self.g.turn_number > 0):
            self.place_pieces()
        if (self.g.gameover == True):
            self.draw_end_symbol()

    def creategrid(self):
        '''Draws the tictactow grid.
        Pre: uses class's canvas object.
        Post: draws lines on the canvas.'''
        ## Drawling Background
        self.canvas.create_rectangle(self.x_offset,self.y_offset,self.x_offset+self.width,self.y_offset+self.height,fill="#C0C0C0")
        ## Drawling Lines
        length = self.width / 3
        # Line 1
        x0 = length + self.x_offset
        y0 = self.y_offset
        x1 = x0
        y1 = self.y_offset + self.height
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)
        # Line 2
        x0 = 2*length + self.x_offset
        y0 = self.y_offset
        x1 = x0
        y1 = self.y_offset + self.height
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)
        # Line 3
        x0 = self.x_offset
        y0 = self.y_offset + length
        x1 = self.x_offset + self.width
        y1 = y0
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)
        # Line 4
        x0 = self.x_offset
        y0 = self.y_offset + 2*length
        x1 = self.x_offset + self.width
        y1 = y0
        self.canvas.create_line(x0,y0,x1,y1,width=4.0)

    def place_pieces(self):
        '''Draws the pieces on the board when necessary.
        Pre: Uses class's canvas and game objects.
        Post: Current pieces in game are are board. '''
        for i in range(0,9,1):
            piece = self.g.board[i]
            if piece != ".":
                self.drawshape(i,piece)

    def WhichSquare(self,event):
        '''Determines which square has been clicked.
        Pre: x and y are the coordinates of the click.
        Post: initiates the takeTurn method from game class.'''
        ## Checking which square was clicked
        # Initial values
        x = event.x
        y = event.y
        coor = "out"
        first_x = self.x_offset + self.width/3
        second_x = self.x_offset + (2*self.width)/3
        third_x = self.x_offset + self.width
        first_y = self.y_offset + self.height/3
        second_y = self.y_offset + (2*self.height)/3
        third_y = self.y_offset + self.height
        # Determing square by coordinates
        if (x > self.x_offset) and (y > self.y_offset):
            if y < first_y:
                if x < first_x:
                    coor = 0 # Top left square.
                elif x < second_x:
                    coor =  1 # Top middle square.
                elif x < third_x:
                    coor = 2 # Top Right square.
            elif y < second_y:
                if x < first_x:
                    coor = 3 # Middle left square.
                elif x < second_x:
                    coor = 4 # Center Square.
                elif x < third_x:
                    coor = 5 # Middle rigth square.
            elif y < third_y:
                if x < first_x:
                    coor = 6 # Bottom left square.
                elif x < second_x:
                    coor = 7 # Bottom Middle square.
                elif x < third_x:
                    coor = 8 # Bottom Right Square.
        
        # Entering move in game
        if coor != "out":
            if self.g.gameover == False:
                current_sym = self.g.turn
                if (self.g.TakeTurn(coor)): # Begins the turn in game class.
                    self.drawshape(coor,current_sym) # Draws shape if valid move
                    self.g.CheckEnd() # Checks to see if game is over
                    self.label_message.set(self.g.message)
                    # Checking whether to draw winning symbol
                    if self.g.gameover == True:
                        self.draw_end_symbol()
                    # If using AI
                    elif self.use_ai == True:
                        current_sym = self.g.turn
                        ai_move = self.a.next_move(self.g.board, self.g.turn)
                        if (self.g.TakeTurn(ai_move)): # Checking move
                            self.drawshape(ai_move,current_sym)
                            self.g.CheckEnd()
                            self.label_message.set(self.g.message)
                            # Checking whether to draw winning symbol
                            if self.g.gameover == True:
                                self.draw_end_symbol()
                        else:
                            print("AI gave bad move.")
                            exit()
                    
                else: # Invalid Move
                    self.label_message.set(self.g.message)
            else:
                self.label_message.set("Game Over, Hit New")

    def draw_end_symbol(self):
        '''Draws the symbol incidicating a window.
        Pre: Uses the game class end_symbol variable.
        Post: Symbol is drawn. '''
        if self.g.end_symbol == -1: # Tie
            x0 = self.x_offset + self.width/6
            y0 = self.y_offset + (self.height)/6
            x1 = self.x_offset + (5*self.width)/6
            y1 = self.y_offset + (5*self.height)/6
            self.canvas.create_arc(x0,y0,x1,y1,style=ARC,width=8.0,start=30.0,extent=300.0,dash=(16,8),outline="#009ACD")
        else:
            if self.g.end_symbol == 0: # Across top
                x0 = self.x_offset + self.width/12
                y0 = self.y_offset + self.height/6
                x1 = self.x_offset + (11*self.width)/12
                y1 = y0
            elif self.g.end_symbol == 1: # Down left
                x0 = self.x_offset + self.width/6
                y0 = self.y_offset + self.height/12
                x1 = x0
                y1 = self.y_offset + (11*self.height)/12
            elif self.g.end_symbol == 2: # Diagonal from top left
                x0 = self.x_offset + self.width/12
                y0 = self.y_offset + self.height/12
                x1 = self.x_offset + (11*self.width)/12
                y1 = self.y_offset + (11*self.height)/12
            elif self.g.end_symbol == 3: # Diagonal from bottom left
                x0 = self.x_offset + self.width/12
                y0 = self.y_offset + (11*self.height)/12
                x1 = self.x_offset + (11*self.width)/12
                y1 = self.y_offset + self.height/12
            elif self.g.end_symbol == 4: # Down right
                x0 = self.x_offset + (5*self.width)/6
                y0 = self.y_offset + self.height/12
                x1 = x0
                y1 = self.y_offset + (11*self.width)/12
            elif self.g.end_symbol == 5: # Across bottom
                x0 = self.x_offset + self.width/12
                y0 = self.y_offset + (5*self.height)/6
                x1 = self.x_offset + (11*self.width)/12
                y1 = y0
            elif self.g.end_symbol == 6: # Down middle
                x0 = self.x_offset + self.width/2
                y0 = self.y_offset + self.height/12
                x1 = x0
                y1 = self.y_offset + (11*self.height)/12
            elif self.g.end_symbol == 7: # Across middle
                x0 = self.x_offset + self.width/12
                y0 = self.y_offset + self.height/2
                x1 = self.x_offset + (11*self.width)/12
                y1 = y0
            # Drawing the line over the winner
            self.canvas.create_line(x0,y0,x1,y1,width=8.0,dash=(16,8),fill="#009ACD")

    def shape_coordinates(self,x,y):
        '''Finds the coordinates for either a circle or cross
        Pre: The center x,y as arguments, also uses current value of self.width.
        Post: The box coordinates are returned as a tuple.'''
        # Finding coordinates
        temp = self.width / 8 # half the length of a side
        x0 = x - temp
        y0 = y - temp
        x1 = x + temp
        y1 = y + temp
        return (x0,y0,x1,y1)

    def circle(self,x,y):
        '''Creates Circle on Board.
        Pre: Center of symbol.
        Post: Draws an O on the board at the center coordinate given.'''
        # Retrieving coordinates
        (x0,y0,x1,y1) = self.shape_coordinates(x,y)
        # Creating circle
        self.canvas.create_oval(x0,y0,x1,y1,outline="#33DD00",width=4.0)

    def cross(self,x,y):
        '''Creates Cross on board.
        Pre: Center is middle position of "X" on board.
        Post: Draws an X on the board at the center coordinate given'''
        # Retrieving coordinates
        (x0,y0,x1,y1) = self.shape_coordinates(x,y)
        # Creating lines
        self.canvas.create_line(x0,y0,x1,y1,fill="#FF3300",width=4.0)
        self.canvas.create_line(x0,y1,x1,y0,fill="#FF3300",width=4.0)

    def drawshape(self,coor,Turn):
        x = None
        y = None
        if coor == 0:            # Top Left
            x = self.width/6
            y = self.height/6
        elif coor == 1:          # Top Middle
            x = self.width/2
            y = self.height/6
        elif coor == 2:          # Top Right
            x = (5*self.width)/6
            y = self.height/6
        elif coor == 3:          # Middle Left
            x = self.width/6
            y = self.width/2         
        elif coor == 4:          # Center
            x = self.width/2
            y = self.width/2
        elif coor == 5:          # Middle Right
            x = (5*self.width)/6
            y = self.width/2
        elif coor == 6:          # Bottom Left
            x = self.width/6
            y = (5*self.width)/6
        elif coor == 7:          # Bottom Middle
            x = self.width/2
            y = (5*self.width)/6
        elif coor == 8:          # Bottom Right
            x = (5*self.width)/6
            y = (5*self.width)/6
            
        # Deciding Between Circle and square.
        if (x != None) and (y != None):
            x += self.x_offset
            y += self.y_offset
            if Turn == "O":      
                self.circle(x,y)
            else:
                self.cross(x,y)

