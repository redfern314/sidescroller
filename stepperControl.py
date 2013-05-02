import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

position = 0

step = [3,5,8,7]
for x in step:
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x,0)

button = [11,12]
GPIO.setup(button[0],GPIO.OUT)
GPIO.output(button[0],1)
GPIO.setup(button[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def setpins(out,x):
	for pin in range(len(out)):
		if not pin in x:
			GPIO.output(out[pin],0)
		else:
			GPIO.output(out[pin],1)

tcons = .002

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

setpins(step,[])

while (position>=0 and position<=630):
	input = GPIO.input(button[1])
	if input:
		up()
		position -= 1
                print 'up'
	else:
		down()
		position += 1
                print 'down'

#player died; time to reset
setpins(step,[])
time.sleep(1)

#go all the way back up
while position>0:
	fwd()
	position -= 1

#deactivate pins to save the power supply and h-bridge
setpins(step,[])

