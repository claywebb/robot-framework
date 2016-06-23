# Written for the Walsh Jesuit Robotics Club
# Copyright (c) 2016

import RPi.GPIO as GPIO
import time

from Modules import CharLCD

class Robot(object):

    __leftWheels = []
    __rightWheels = []
    __IRLEDs = []

    # Boolean set variables
    __isset_LCD = False


    def __init__(self, arg0):
        print "Configuring Robot"
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
        print "move"
        # arg0 is speed
        # arg1 is time (optional)

    def turn(self, arg0, arg1):
        print "turn"
        # arg0 is change in degree (positive is clockwise, negative is counterclockwise)
        # arg1 is speed at which to pivot

    def moveDistance(self, arg0):
        print "move distance"
        # arg0 is distance in feet

    #############################################################
    # IR LED Collision Detection Methods
    #############################################################

    def checkForCollisionLR(self, arg0, arg1):
        # check for collision among two left/right or front/back IR LEDs
        i=GPIO.input(arg0)                        #Reading output of right IR sensor
        j=GPIO.input(arg1)                        #Reading output of left IR sensor
        if i==0:                                  #Right IR sensor detects an object
            print("Obstacle detected on Left",i)
            return -1
            time.sleep(0.1)
        elif j==0:                                #Left IR sensor detects an object
            print ("Obstacle detected on Right",j)
            return 1
            time.sleep(0.1)
        else:
            return 0

    def checkForCollision(self):
        # check for collision among a list of IR LEDs
        if len(self.__IRLEDs) == 0:                                     # If no IR LEDs are set then display an warning
            print "Warning: Checking for collision but no IR LEDs are set!"

        for x in self.__IRLEDs:
            if GPIO.input(x)==i:
                print("Obstacle detected with LED on Pin %s" % arg0[i.index(x)])
                return arg0[i.index(x)]
                time.sleep(0.1)
        return 0

    #############################################################
    # LCD Display Methods
    #############################################################

    def addLCDScreen(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6):
        # the arguments in order are pin_rs, pin_e
        self.__LCD = CharLCD(arg0, arg1, arg2, arg3, arg4, arg5, arg6)        # Add and initialize the LCD screen
        self.__LCD.begin(16,2)                                          # Specify the dimensions of the screen (row,col)
        self.__isset_LCD = True            # Set the variable so the rest of the software knows there is a LCD connected


    def writeToLCD(self, arg0):
        # Write a string (arg0) to the LCD display
        # The newline character (\n) separates the lines
        if self.__isset_LCD == False:
            print "Error: Can not write to LCD because there is no LCD configured"
            return 0
        self.__LCD.clear()                                              # Clear the display before showing anything
        self.__LCD.message(arg0)

    def clearLCD(self):
        if self.__isset_LCD == False:
            print "Error: Can not clear LCD because there is no LCD configured"
            return 0
        self.__LCD.clear()