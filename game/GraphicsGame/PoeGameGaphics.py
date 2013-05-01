"""
The Graphical world for the game
"""

from PoeGame import *
import Tkinter, ImageTk, Image
import random

class GraphicModifier(Modifier):

    def __init___(self, location, typeEffect = None):
        self.type = self.chooseType()
        print self.type
        Modifier.__init__(self)

    def chooseType(self):
        if random.random()<.5:
            return 'poison'
        return 'bonus'

"""
Graphic implementation of World class (child class of World)
Controls the World object in C
"""
class GraphicWorld(World):
    
    def __init__(self):
        self.modifiers = []
        self.worldGrid = self.buildWorld((800,600))
        World.__init__(self)


    def __string__(self):
        return self

    '''
    Builds the grid representing the world upon initiation.
    Takes the dimensions of the world
    Returns a list of lists representing an array of the world
    Where the index of each list is x-position
    and each list represents a collumn
    '''   
    def buildWorld(self, dimensions):
        self.gridCoords = (dimensions[0]/10, dimensions[1]/10)
        worldGrid = [[]]
        for i in range(self.gridCoords[1]):
            worldGrid[0].append(0)
        for i in range(self.gridCoords[1]/4):
            worldGrid[0][i] =1
            worldGrid[0][-1*(i+1)]=1
        currentTop = self.gridCoords[1]/4
        currentBottom = self.gridCoords[1]/4*3
        for i in range(1,self.gridCoords[0]):
            newCollumn = self.buildCollumn(currentTop, currentBottom)
            worldGrid.append(newCollumn[0])
            currentTop=newCollumn[1]
            currentBottom = newCollumn[2]
        return worldGrid

    """
    Updates the graphic world as the world scrolls
    Assumes left to right movement
    """
    def updateWorld(self):
        lastCollumn = self.worldGrid[-1]
        currentTop = lastCollumn.index(0)
        currentBottom = lastCollumn.count(0)+lastCollumn.index(0)
        self.worldGrid.append(self.buildCollumn(currentTop,currentBottom)[0])
        self.worldGrid.pop(0)

        
        
    """
    Builds a collumn in the grid representing the world
    Takes from the previous collumn (previous top of
    space and previous bottom of space) and uses random number
    generation to determine the location of the ceiling.
    Returns an array representing the new collumn; the new
    ceiling; the new floor
    """
    def buildCollumn(self, prevTop, prevBottom):
        newTop = prevTop + random.randint(-1,1)
        newBottom = prevBottom + random.randint(-1,1)
        newCollumn = []
        for i in range(self.gridCoords[1]):
            newCollumn.append(0)
        if (newTop<=0):
            newTop = 5
        if (newBottom>(self.gridCoords[1] - 1)):
            newBottom = self.gridCoords[1]-5
        if (newCollumn.count(0) < 8):
            newTop+=8
            newBottom-=8
        for i in range(newTop):
            newCollumn[i]=1
        for j in range(newBottom,60):
            newCollumn[j]=1
        if self.hasModifier():
            newMod = self.addModifier(newTop, newBottom)
            newCollumn[newMod[0]]= newMod[1]
        return (newCollumn, newTop, newBottom)

    def hasModifier(self):
        if random.random()>.99:
            return True
        return False

    def addModifier(self, upperBound, lowerBound):
        #print "foo"
        position = random.randint(upperBound, lowerBound)
        m = GraphicModifier(position)
        print m.type 
        self.modifiers.append(m)
        if m.type == 'bonus':
            return (position, 2)
        if m.type == 'poison':
            return (position, 3)

        #self.modifiers.append(Modif
        

        
    
def main():
    myWorld = GraphicWorld()
    myWorld.updateWorld()

main()
        

        
class GraphicSnail(Snail):

    def __init__(self):
        Snail.__init__(self)
