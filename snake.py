import tkinter
import random
import threading
import queue


class Snake:
    def __init__(self ,main_window, board , width , height):
        self.snakesize = 1
        self.speed = 0.02
        self.snakelength = 10
        self.currentlength = 1
        self.path = queue.deque()
        self.height=height
        self.width=width
        self.board = board
        self.main = main_window
        self.foodposX = None
        self.foodposY = None
        self.directions = ['L' , 'R' , 'U' , 'D']
        self.current_direction = self.directions[random.randrange(0 , 4 , 1)]
        self.posX = random.randrange(0 , width , 1)
        self.posY = random.randrange(0 , height , 1)
        self.path.append((self.posX , self.posY))
        self.board.create_oval(self.posX, self.posY, self.posX+self.snakesize, self.posY +self.snakesize)
        main_window.bind('<Key>', self.changeDirection) 
        self.crawl()
        self.food()
   
        
    def nextPosition(self):
        
        if (self.current_direction == 'L'):
            self.posX = (self.posX-1 )%self.width 
        elif (self.current_direction == 'R'):
            self.posX = (self.posX+1 )%self.width 
        elif (self.current_direction == 'U'):
            self.posY = (self.posY-1)%self.height
        elif (self.current_direction == 'D'):
            self.posY = (self.posY+1)%self.height
            
        #if touches itself
        if (self.posX , self.posY) in self.path:
            self.lost()
        #if ate food
        if (self.posX  == self.foodposX ) and (self.posY == self.foodposY ):
            self.food()
            self.snakelength += self.snakesize*2
            
        self.path.append((self.posX , self.posY))
        
        if (self.currentlength<= self.snakelength):
            self.board.create_oval(self.posX, self.posY, self.posX+self.snakesize, self.posY+self.snakesize )
            self.currentlength +=1
        else:
            self.path.popleft()
            self.board.delete("all")
            for (x,y) in self.path:
                self.board.create_oval(x, y, x+self.snakesize, y+self.snakesize)
                self.board.create_oval(self.foodposX, self.foodposY, self.foodposX+self.snakesize, self.foodposY+self.snakesize )
        
        
          
    def changeDirection(self ,  event):
        if (event.keysym == "Up"):
            self.current_direction = 'U'
        elif (event.keysym == "Down"):
            self.current_direction = 'D'
        elif (event.keysym == "Left"):
            self.current_direction = 'L'
        elif (event.keysym == "Right"):
            self.current_direction = 'R'
        elif (event.keysym == "Escape"):
            self.stop()
            
    def food(self):
        self.foodposX = random.randrange(0 , self.width , 1)
        self.foodposY = random.randrange(0 , self.height , 1)
        self.board.create_oval(self.foodposX, self.foodposY, self.foodposX+self.snakesize, self.foodposY+self.snakesize )
            
    def crawl(self):
        self.loop = threading.Timer(self.speed , self.crawl)
        self.loop.start()
        self.nextPosition()
        
    def stop(self):
        self.loop.cancel()
        self.main.destroy()
        
    def lost(self):
        self.loop.cancel()
        self.board.create_text(self.width/2 , self.height/2 , text= "Lost!" , font= ('Helvetica', 40, 'bold'))
        

class Board:
    def __init__(self , main_window):
        self.height=400
        self.width=600
        self.canvas =  tkinter.Canvas(main_window,  height=self.height, width=self.width)
        self.canvas.pack()
        self.snake = Snake(main_window , self.canvas , self.width , self.height)
        
        
        
        
        
class Game:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("🅢🅝🅐🅚🅔")
        self.board = Board(self.window)
        self.window.mainloop()
    
Game()


