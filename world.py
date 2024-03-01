from turtle import position
from settings import *
from window import *
from stack import *
import time

class PositionNode():
    def __init__(self, x, y):
        self.position = (x, y)
        self.direction = 0

class World:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.player = None
        self.end = None
        self.stack = Stack(100)
    
  
        
    def BuildMaze(self):
        x = y =0
        for row in range(len(GRID)):
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
                    self.stack.push(PositionNode(row, col))
                    
    def FindPath(self):
        v_list = []
        while not self.stack.isEmpty():
            currentNode = self.stack.pop()
            
            row, col = currentNode.position
            d = currentNode.direction
            currentNode.direction += 1           
            self.stack.push(currentNode)
            
            if MAP[row][col] == "E":
                for node in self.stack.stack:
                    if node == None:
                        break
                    x, y = node.position
                    MAP[x][y] = "P"
                return True
            
            if d == 0:
                if self.getNextCell(row - 1, col) and (row - 1, col) not in v_list:
                    self.stack.push(PositionNode(row - 1, col))
                    v_list.append((row, col))
             
            elif d == 1:
                if self.getNextCell(row, col - 1) and (row, col - 1) not in v_list:
                    self.stack.push(PositionNode(row, col - 1))
                    v_list.append((row, col))
                   
            elif d == 2:
                if self.getNextCell(row + 1, col) and (row + 1, col) not in v_list:
                    self.stack.push(PositionNode(row + 1, col))
                    v_list.append((row, col))
            
            elif d == 3:
                if self.getNextCell(row, col + 1) and (row, col + 1) not in v_list:
                    self.stack.push(PositionNode(row, col + 1))
                    v_list.append((row, col))
            
            else:
                v_list.append((row, col))
                self.stack.pop()
        self.stack.display() 
        return False


    def getNextCell(self, row, col):
        try:
            nextCell = MAP[row][col]
            if nextCell != "#": return True
        except:
            print("Error")      
        return False
                
                
                
        
    def RunWorld(self):
        
        self.BuildMaze()
        if self.FindPath():
            self.stack.reverse()
            

        while True:
            self.window.screen.update()
           
            if not self.stack.isEmpty():
                node = self.stack.pop()
                x,y = node.position
                
                y = LEFT + (y * 25)
                x = TOP - (x * 25)
                self.window.DrawPlayer(y + 25, x - 25)
                time.sleep(0.1)
      

world = World()
world.RunWorld()
        
        
        