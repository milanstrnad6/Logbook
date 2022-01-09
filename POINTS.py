#MANAGER:HISTORY

import FILES
import TIMES

#PROPERTIES

FILENAME = '/home/pi/Desktop/Logbook4/Logbook/points.txt'

#ACTIONS: LOAD

def load_allEvents():
    return FILES.load(FILENAME)

def getClearPointString(rideKey):
	return rideKey + "|" + TIMES.stringFrom(TIMES.now()) + "\n"

def getPointString(rideKey,north,east):
    return rideKey + "|" + "N" + north + "|" + "E" + east + "|" + TIMES.stringFrom(TIMES.now()) + "\n"

#ACTIONS: SAVE

def saveClearPoint(rideKey):
	data = FILES.load(FILENAME)
	point = getClearPointString(rideKey)
	data.append(point)
	FILES.save(FILENAME,data)

def savePoint(rideKey,north,east):
    data = FILES.load(FILENAME)
    point = getPointString(rideKey,north,east)
    data.append(point)
    FILES.save(FILENAME,data)

def reset():
    data = ""
    FILES.save(FILENAME,data)