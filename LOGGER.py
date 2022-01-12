import FILES
import TIMES
import VALUES

FILENAME_CURRENT_RIDE = '/home/pi/Desktop/Logbook4/Logbook/currentRide.txt'
FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEURLPATH = 0
FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEKEY = 1
FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT = 2
FILENAME_CURRENT_RIDE_ROW_INDEX_FIRSTLOCATIONSENT = 3
FILENAME_CURRENT_RIDE_ROW_INDEX_LASTN = 4
FILENAME_CURRENT_RIDE_ROW_INDEX_LASTE = 5
FILENAME_CURRENT_RIDE_ROW_INDEX_DISTANCE = 6

FILENAME_BASE = '/home/pi/Desktop/Logbook4/Logbook/base.txt'
FILENAME_BASE_ROW_NUMBEROFRIDES = 0

def logNewRide():
    FILES.resetWithData(FILENAME_CURRENT_RIDE,"0\n1\n2\n3\n4\n5\n6\n")
    rideUrlPath = VALUES.rideUrlPath()
    rideKey = VALUES.rideKey()
    rideSent = "0"
    firstLocationSent = "0"
    lastN = "0.0"
    lastE = "0.0"
    distance = "0.0"
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEURLPATH,rideUrlPath)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEKEY,rideKey)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT,rideSent)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_FIRSTLOCATIONSENT,firstLocationSent)

    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_LASTN,lastN)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_LASTE,lastE)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_DISTANCE,distance)

    newNumberOfRides = numberOfRides() + 1
    newNumberOfRidesAsString = str(newNumberOfRides)
    FILES.saveline(FILENAME_BASE,FILENAME_BASE_ROW_NUMBEROFRIDES,newNumberOfRidesAsString)

def setRideSent(sent):
    rideSent = str(sent)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT,rideSent)

def setFirstLocationSent(sent):
    firstLocationSent = str(sent)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_FIRSTLOCATIONSENT,firstLocationSent)

def setLastN(lastN):
    lastNString = str(lastN)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_LASTN,lastNString)

def setLastE(lastE):
    lastEString = str(lastE)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_LASTE,lastEString)

def setDistance(distance):
    distance = str(distance)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_DISTANCE,distance)

def rideUrlPath():
    #return "2021/1/1/7"
    return FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEURLPATH).rstrip("\n")

def rideKey():
    #return "2021-01-07 19:54:43"
    return FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEKEY).rstrip("\n")

def rideSent():
    rideSent = FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT).rstrip("\n")
    return int(rideSent)

def firstLocationSent():
    rideSent = FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_FIRSTLOCATIONSENT).rstrip("\n")
    return int(rideSent)

def numberOfRides():
    numberOfRides = FILES.loadline(FILENAME_BASE,FILENAME_BASE_ROW_NUMBEROFRIDES)
    return int(numberOfRides)

def lastN():
    lastN = FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_LASTN).rstrip("\n")
    print(lastN)
    return float(lastN)

def lastE():
    lastE = FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_LASTE).rstrip("\n")
    print(lastE)
    return float(lastE)

def distance():
    distance = FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_DISTANCE).rstrip("\n")
    return float(distance)

def resetBaseFile():
    data = "0"
    FILES.save(FILENAME_BASE,data)