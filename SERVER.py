#BOOT MODULE:SERVER

import subprocess as SUB
import time

#ACTIONS

def boot():
    duration = 5 #WAIT FOR INTERNET CONNECTION
    time.sleep(duration)
    SUB.call(['/home/pi/Desktop/Logbook/serverStart.sh'])

#MAIN

boot()
