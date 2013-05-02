import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

dir = [15,16]
move = 18

for x in dir:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x,0)

GPIO.setup(move,GPIO.OUT)
pwm = GPIO.PWM(move, 20)
pwm.start(0)

print 'Command: '
ans = raw_input().strip()
while not ans == 'end':
    if ans == 'dir':
        for x in dir:
            GPIO.output(x,0)
        print 'New dir:'
        ans = raw_input().strip()
        GPIO.output(dir[int(ans)],1)
    else:
        pwm.ChangeDutyCycle(int(ans))
    ans = raw_input().strip()
