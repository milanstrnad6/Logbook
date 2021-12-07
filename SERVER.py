#BOOT MODULE:SERVER

import subprocess as SUB
import time

import DATA

#ACTIONS

def boot():
    duration = 5 #WAIT FOR INTERNET CONNECTION
    time.sleep(duration)
    SUB.call(['/home/pi/Desktop/GPSFINAL/Logbook/serverStart.sh'])

#MAIN

boot()
