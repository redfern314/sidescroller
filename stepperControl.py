import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

step = [3,5,8,7]
for x in step:
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x,0)

button = [11,12]
GPIO.setup(button[0],GPIO.OUT)
GPIO.output(button[0],1)
GPIO.setup(button[1],GPIO.IN)

def setpins(out,x):
	for pin in range(len(out)):
		if not pin in x:
			GPIO.output(out[pin],0)
		else:
			GPIO.output(out[pin],1)

tcons = .001

def fwd():
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

def bkwd():
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

'''for a in range(100):
	fwd()

for a in range(100):
	bkwd()'''

setpins(step,[])

for i in range(2000):
	input = GPIO.input(button[1])
	if input:
		fwd()
	else:
		setpins(step,[])
		time.sleep(.1)

setpins(step,[])
