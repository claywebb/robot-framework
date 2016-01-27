import RPi.GPIO as GPIO
import time

class Robot(object):

    __leftWheels = []
    __rightWheels = []
    __IRLEDs = []


    def __init__(self, arg0):

        # arg0 is a dictionary, which means it is a list with keys and values (key:value, key:value, ...)
        # the key is the type of peripheral is plugged into the board
        # the value is the pin number it is plugged into

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        for key, value in arg0:
            if key == "LEFTWHEEL":
                self.__leftWheels.append(value)
                continue
            if key == "RIGHTWHEEL":
                self.__rightWheels.append(value)
                continue
            if key == "IRLED":
                self.__IRLEDs.append(value)
                continue

        GPIO.setup(3, GPIO.IN)                            #Right sensor connection
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left sensor connection

    # Move Function (forward and back)
    def move(self, arg0, arg1):
        # arg0 is speed
        # arg1 is time (optional)

    def turn(self, arg0, arg1):
        # arg0 is change in degree (positive is clockwise, negative is counterclockwise)
        # arg1 is speed at which to pivot

    def moveDistance(self, arg0):
        # arg0 is distance in feet

    def checkForCollisionLR(self, arg0, arg1):
        # check for collision among two left/right or front/back IR LEDs
        i=GPIO.input(arg0)                         #Reading output of right IR sensor
        j=GPIO.input(arg1)                        #Reading output of left IR sensor
        if i==0:                                #Right IR sensor detects an object
            print("Obstacle detected on Left",i)
            return -1
            time.sleep(0.1)
        elif j==0:                              #Left IR sensor detects an object
            print ("Obstacle detected on Right",j)
            return 1
            time.sleep(0.1)
        else:
            return 0

    def checkForCollision(self, arg0):
        # check for collision among a list of IR LEDs
        for x in arg0:
            if GPIO.input(x)==i:
                print("Obstacle detected with LED on Pin %s" % arg0[i.index(x)])
                return arg0[i.index(x)]
                time.sleep(0.1)
        return 0


