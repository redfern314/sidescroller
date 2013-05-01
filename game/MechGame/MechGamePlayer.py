"""
Mechanical PoeGame Player
"""
from PoeGameMechanical import *
import time
import matplotlib
import threading
from Tkinter import *
#import main as vision
#import rpiControl as raspPiController

"""
Assumptions:
Pass data every 100 ms
Approximately 130x133
"""
class Game():

    """
    Takes a raspPiController object
    Initialises the start state of all elements
    Begins the Game loop
    """
    def __init__(self, raspPiController):
        self.world = MechanicalWorld()
        self.snail = MechanicalSnail()
        self.master = Tk()
        self.counter = 0
        self.isRunning =True
        self.playGame()

    """
    Runs the main loop of the game
    Includes callback function for the snail
    """
    def playGame(self):
        def callback(event):
            self.snail.isLift = True
            self.snail.lifCounter = 0
        self.master.bind('<Return>', callback)
        while self.isRunning == True:
            runWorld()
            

    """
    A 100 ms loop for the game
    Updates the World state, then moves the snail, checks for
    collisions, increments speed if necissary, and adds points.
    """
    def runWorld(self):
        """Callback function for Lift event"""
        self.world.updateWorld()
        self.snail.move()
        if self.detectCollision():
            self.isRunning = False
            return
        if self.counter>2000:
            self.world.setSpeed(self.world.speed+.5)
        self.counter+=100
        self.world.points+=5
        #send data to rasp pi
        #raspPiController.setSnailPostions(self.sendSnailPosition())
        time.sleep(.1)
        
    """
    Checks for collision with ceiling or floor
    """
    def detectCollision(self):
        snailGridLocation = self.snail.getGridLocation()
        #numpy doesn't provide an indexOf function :(
        for i in range(4):
            if self.world.grid[snailGridLocation[0]][snailGridLocation[1]+i]==1:
                return True
            if self.world.grid[snailGridLocation[0]][snailGridLocation[1]-i]==1:
                return True
        return False
        

    """
    Set of Methods relating to Raspberry Pie output
    """

    """
    Sends World speed in inches per second
    """
    def sendWorldSpeed(self):
        return self.world.speed

    """
    Sends Snail net movement rate in inches per second
    """
    def sendSnailSpeed():
        if self.snail.isLift:
            return self.snail.liftRate + self.snail.fallRate
        return self.snail.fallRate

    """
    Adjusts the snail's position to a 0-100 scale
    and sends the snails position to the raspberry pi
    """
    def sendSnailPosition():
        return self.snail.position[1]

    
