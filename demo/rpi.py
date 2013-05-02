import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

position = None #in pixels
px_per_step = None

step = [3,5,8,7]
mdir = [15,16]
move = 18

for x in step:
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x,0)
for x in mdir:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x,0)
GPIO.setup(move, GPIO.OUT)
pwm = GPIO.PWM(move, 20)
pwm.start(0)


button = [11,12]
GPIO.setup(button[0],GPIO.OUT)
GPIO.output(button[0],1)
GPIO.setup(button[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

tcons = .002

#dont do anything to start
setpins(step,[])

def setpins(out,x):
	for pin in range(len(out)):
		if not pin in x:
			GPIO.output(out[pin],0)
		else:
			GPIO.output(out[pin],1)

def down():
	setpins(step,[0,3])  
        time.sleep(tcons)
	setpins(step,[0])  
        time.sleep(tcons)
	setpins(step,[0,2])  
        time.sleep(tcons)
	setpins(step,[2])  
        time.sleep(tcons)
	setpins(step,[1,2])  
        time.sleep(tcons)
	setpins(step,[1])  
        time.sleep(tcons)
	setpins(step,[1,3])  
        time.sleep(tcons)
	setpins(step,[3])
        time.sleep(tcons)	

def up():
	setpins(step,[1,3])
        time.sleep(tcons)
	setpins(step,[1])
        time.sleep(tcons)
	setpins(step,[1,2])
        time.sleep(tcons)
	setpins(step,[2])     
        time.sleep(tcons)
	setpins(step,[0,2])
        time.sleep(tcons)
	setpins(step,[0])
        time.sleep(tcons)
	setpins(step,[0,3])
        time.sleep(tcons)
	setpins(step,[3])
        time.sleep(tcons)

def goForward():
	GPIO.output(mdir[1], 0)
	GPIO.output(mdir[0], 1)

def goBackward():
	GPIO.output(mdir[0], 0)
	GPIO.output(mdir[1], 1)

#these functions are the only ones that should be called from outside
def initialize(init_pos, available_steps):
	position = init_pos
	px_per_step = init_pos/available_steps

def getInput():
	return GPIO.input(button[1])

def changeSpeed(thespeed):
	pwm.ChangeDutyCycle(thespeed)

def changeDir(thedir):
	if(thedir):
		goForward()
	else:
		goBackward()

def moveTo(pos): #pos will be in pixels
	while(position > pos + px_per_step/2 | position < pos - px_per_step/2):
		if(pos > position):
			down()
			position += px_per_step
		else:
			up()
			position -= px_per_step
	#deactivate pins to save the power supply and h-bridge
	setpins(step,[])

