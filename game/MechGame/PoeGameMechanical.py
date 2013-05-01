"""
PoeGameMechanical
All measurements in inches, inches/second
"""

from PoeGame import *
import random
import matplotlib
import main as vision

class MechanicalWorld(World):

    """
    MechWorld Constructor
    """
    def __init___(self):
        World.__init__(self)
        #self.visionCollector = visionCollector()
        self.speed = 1.0
        self.gravity = 2.0
        self.maxSpeed = 10.0
        self.grid = updateWorld(buildMechanicalWorld())
        

    """
    On construction, gathers data from the vision
    system. Builds the world and sets the grid coordonites 
    """
    def buildMechanicalWorld(self):
        return vision.initialize()

    """
    Gets a reading from the vision system to update
    the world matrix
    """
    def updateWorld(self,visionData):
        return vision.getReading()

    """
    Sets the speed at which the world is moving,
    in inches per second
    """
    def setSpeed(self,newSpeed):
        if self.speed<self.maxSpeed:
            self.speed = self.newSpeed


class MechanicalSnail(Snail):

    """
    Constructor for a mechanical implementation of the
    snail. 
    """
    def __init__(self):
        Snail.__init__(self)
        self.location = (9.0,12.0)
        self.fallRate = 2.0 #in inches per second
        self.liftRate = -6.0 #in inches per second
        self.isLift = False
        self.liftCounter = 0
        self.gridLocation = self.updateGridLocation()

    """
    Gets the snail's locatioin relative to the vision grid
    """
    def getGridLocation(self):
        return ((self.vision.getReading().shape[0]/self.location[0]),
                (self.vision.getReading().shape[1]/self.location[1]))

    """
    Checks if the snail is being lifted, and moves it accordingly
    """
    def move(self):
        if self.isLift:
            self.fall()
            self.lift()
        else:
            self.fall()

    
    def fall(self):
        self.location = (self.location[0],self.location[1]+self.fallRate/10)

    def lift(self, lift = None):
        if not lift:
            lift = self.liftRate
        self.location = (self.location[0],self.location[1]+self.liftRate/10)


        


