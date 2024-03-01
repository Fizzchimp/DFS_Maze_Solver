from settings import *
from window import *
import time

class World:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.player = None
        self.end = None
    
  
        
    def BuildMaze(self):
        x = y =0
        for row in range( len(GRID ) ):
            for col in range( len(GRID[row])):
                grid_mark = GRID[row][col]
                x = LEFT + ( col * 25)
                y = TOP - (row * 25)
                

                
                if grid_mark == "#":
                    self.window.DrawWall(x + IMAGE_OFFSET, y - IMAGE_OFFSET)
                
                    
                if grid_mark == "E":
                    self.end = (x,y)
                    self.window.DrawEnd(x + IMAGE_OFFSET, y - IMAGE_OFFSET)
                
                if grid_mark == "S":
                    self.player = (x,y)
                    self.window.DrawPlayer(x + IMAGE_OFFSET,y - IMAGE_OFFSET)
                   
                    
                    
                
                
                
        
    def RunWorld(self):
        
        self.BuildMaze()
        
        # game loop
        while True:
            self.window.screen.update()
      
        

world = World()
world.RunWorld()
        
        
        