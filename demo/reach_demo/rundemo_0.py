#our stuff
import viz
import rpi
import game
#other stuff
import numpy
import time

#list of global variables
ws = None
aworld = None
asnail = None

def checkCollision():
    if(asnail.position < 0 | asnail.position > ws[3]): #checks if snail is outside frame
        return True
    snailGridLocation = asnail.getGridLocation()
    for i in range(4):
        if aworld.grid[snailGridLocation[0]][snailGridLocation[1]+i]==1:
            return True
        if aworld.grid[snailGridLocation[0]][snailGridLocation[1]-i]==1:
            return True
    return False

def beDead():
    rpi.changeSpeed(0)

def main(fps):
	aworld.grid = viz.getReading(ws)
	asnail.isLift = rpi.getInput()
	asnail.move()
	if(checkCollision()):
		return False
	#check power-up
	rpi.changeSpeed(aworld.speed)
	rpi.changeDir(aworld.direction)
	rpi.moveTo(asnail.location)
	time.sleep(1/fps)
	return True

if __name__=='__main__':
	fps = 10

	ws = viz.initialize()
	rpi.initialize(0, 100) #need to give steps in physical range
	aworld = World(50)
	asnail = Snail(0, ws[2]/2) #starts at top center of map
	while(main(fps)): #game loop
		pass
	beDead()
