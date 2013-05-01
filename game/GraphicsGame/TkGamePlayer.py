"""
tkinter game implementation
"""

from Tkinter import *
from PoeGameGaphics import *
import time
import Image, ImageTk

class Game(object):

    def __init__(self):
        self.world = GraphicWorld()
        self.snail = GraphicSnail()
        self.master = Tk()
        self.canvas = Canvas(width = 800, height = 600)
        self.canvas.pack()
        def callback(event):
            self.snail.onEventLift()
        self.master.bind('<Return>', callback)
        self.t = 0
        self.cycle = 0
        self.runWorld()
        self.master.mainloop()

    def runWorld(self):
        self.canvas.delete(ALL)
        self.buildVisualWorld()
        self.world.updateWorld()
        self.canvas.create_rectangle(self.snail.location[0]-25,self.snail.location[1]-25,
                                     self.snail.location[0]+25,self.snail.location[1]+25, fill = "red")
        self.snail.fall()
        if self.detectCollision():
            print self.world.points
            return
        if self.cycle > 2000:
            self.world.setSpeed(self.world.speed-10)
            self.snail.setFallRate(self.world.speed/10)
            self.cycle = 0
        self.cycle+=self.world.speed
        self.world.points+=self.world.pointsRate
        self.master.after(self.world.speed, self.runWorld)

    def buildVisualWorld(self):
        i = 0
        for collumn in self.world.worldGrid:
            ceiling = (collumn.index(0)-1)*10
            floor = (ceiling+collumn.count(0)*10)
            self.canvas.create_rectangle(i,0,i+10,ceiling, fill = "black")
            self.canvas.create_rectangle(i,floor,i+10,600, fill = "black")
            if 2 in collumn:
                self.canvas.create_rectangle(i, collumn.index(2)*10, i+10, collumn.index(2)*10-10, fill = "red")
            if 3 in collumn:
                self.canvas.create_rectangle(i, collumn.index(3)*10, i+10, collumn.index(3)*10-10, fill = "green")
            i +=10
            
    def detectCollision(self):
        snailUpper = []
        snailLower = []
        #snailLeft =[]
        snailFront = []
        for i in range(50):
            snailUpper.append((self.snail.location[0]+i-25,self.snail.location[1]+25))
            snailLower.append((self.snail.location[0]+i-25,self.snail.location[1]-25))
            snailFront.append((self.snail.location[0]+25, self.snail.location[1]+i-25))
        for location in snailUpper:
            if self.world.worldGrid[location[0]/10][location[1]/10] == 1:
                return True
            if self.world.worldGrid[location[0]/10][location[1]/10] == 2:
                self.clearItem()
                self.activatePoison()
                break
            if self.world.worldGrid[location[0]/10][location[1]/10] == 3:
                self.clearItem()
                self.activateBonus()
                break
        for location in snailLower:
            if self.world.worldGrid[location[0]/10][location[1]/10] == 1:
                return True
            if self.world.worldGrid[location[0]/10][location[1]/10] == 2:
                self.clearItem()
                self.activatePoison()
                break
            if self.world.worldGrid[location[0]/10][location[1]/10] == 3:
                self.clearItem()
                self.activateBonus()
                break
        for location in snailFront:
            if self.world.worldGrid[location[0]/10][location[1]/10] == 1:
                return True
            if self.world.worldGrid[location[0]/10][location[1]/10] == 2:
                self.clearItem()
                self.activatePoison()
                break
            if self.world.worldGrid[location[0]/10][location[1]/10] == 3:
                self.clearItem()
                self.activateBonus()
                break
        return False

    def activateBonus(self):
        #self.world.modifiers[-1].chooseEffect()
        print self.world.points
        self.world.points+=50
        print self.world.points

    def activatePoison(self):
        print self.world.points
        self.world.points += -50
        print self.world.points

    def clearItem(self):
        self.world.worldGrid[self.snail.location[0]/10][self.snail.location[1]/10] = 0
        
        
def main():
    game = Game()
    

main()
