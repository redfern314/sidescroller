import RPi.GPIO as GPIO

class rpiControl(object):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3,GPIO.OUT)
        self.pwm = GPIO.PWM(3, 20)
        self.pwm.start(0);

    ''' speed is an integer between 0 and 100
        0 stops the world
        100 is full speed '''
    def setWorldSpeed(speed):
        self.pwm.ChangeDutyCycle(speed)

    ''' pos is an integer between 0 and 100
        0 means the snail is at the bottom
        100 means the snail is at the top '''
    def setSnailPosition(pos):
        # todo: implement stepper functionality
        pass
    
# example code to implement this class:
#   from rpiControl import *
#   control = rpiControl()
#   control.setWorldSpeed(75)
#   control.setSnailPosition(25)