#MANAGER:HISTORY

import FILES
import TIMES
import LOGGER
import geopy.distance

#PROPERTIES

FILENAME = '/home/pi/Desktop/Logbook4/Logbook/points.txt'

#ACTIONS: LOAD

def load_allEvents():
    return FILES.load(FILENAME)

def getNOLOCATIONString(rideKey):
	return "|NOLOCATION|" + TIMES.stringFrom(TIMES.now()) + "\n"

def getPOINTString(rideKey,north,east):
    return "N" + north + "|" + "E" + east + "|" + TIMES.stringFrom(TIMES.now()) + "\n"

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

def updateDISTANCE(northValue,eastValue):
    distance = LOGGER.distance
    print("DISTANCE=")
    print(distance)
    lastN = LOGGER.lastN()
    lastE = LOGGER.lastE()
    if lastN != 0.0:
        coord1 = (lastN, lastE)
        print("LAST N=")
        print(lastN)
        print("LAST E=")
        print(lastE)
        print("northValue=")
        print(northValue)
        print("eastValue=")
        print(eastValue)
        coord2 = (northValue, eastValue)
        result = geopy.distance.geodesic(coord1, coord2)
        print("RESULT=")
        print(result)
        newDistance = distance + result
        LOGGER.setDistance(newDistance)
    else:
        LOGGER.setLastN(northValue)
        LOGGER.setLastE(eastValue)

def reset():
    data = ""
    FILES.save(FILENAME,data)