#MANAGER:HISTORY

import FILES
import TIMES

#PROPERTIES

FILENAME = '/home/pi/Desktop/Logbook4/Logbook/points.txt'

#ACTIONS: LOAD

def load_allEvents():
    return FILES.load(FILENAME)

def getNOLOCATIONString(rideKey):
	return rideKey + "|NOLOCATION|" + TIMES.stringFrom(TIMES.now()) + "\n"

def getPOINTString(rideKey,north,east):
    return rideKey + "N" + north + "|" + "E" + east + "|" + TIMES.stringFrom(TIMES.now()) + "\n"

#ACTIONS: SAVE

def saveNOLOCATION(rideKey):
	data = FILES.load(FILENAME)
	point = getNOLOCATIONString(rideKey)
	data.append(point)
	FILES.save(FILENAME,data)

def savePOINT(rideKey,north,east):
    data = FILES.load(FILENAME)
    point = getPOINTString(rideKey,north,east)
    data.append(point)
    FILES.save(FILENAME,data)

def reset():
    data = ""
    FILES.save(FILENAME,data)