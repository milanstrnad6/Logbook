import FILES
import TIMES
import VALUES

#FILENAME_CURRENT_RIDE = '/home/pi/Desktop/Logbook2/Logbook/currentRide.txt'

FILENAME_CURRENT_RIDE = 'currentRide.txt'
FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEURLPATH = 0
FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEKEY = 1
FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT = 2

FILENAME_BASE = 'base.txt'
FILENAME_BASE_ROW_NUMBEROFRIDES = 0

def logNewRide():
    FILES.resetWithData(FILENAME_CURRENT_RIDE,"0\n1\n2\n")
    rideUrlPath = VALUES.rideUrlPath()
    rideKey = VALUES.rideKey()
    rideSent = "0"
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEURLPATH,rideUrlPath)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEKEY,rideKey)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT,rideSent)

    newNumberOfRides = numberOfRides() + 1
    newNumberOfRidesAsString = str(newNumberOfRides)
    FILES.saveline(FILENAME_BASE,FILENAME_BASE_ROW_NUMBEROFRIDES,newNumberOfRidesAsString)

def setRideSent(sent):
    rideSent = str(sent)
    FILES.saveline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT,rideSent)

def rideUrlPath():
    #return "2021/1/1/7"
    return FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEURLPATH).rstrip("\n")

def rideKey():
    #return "2021-01-07 19:54:43"
    return FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDEKEY).rstrip("\n")

def rideSent():
    rideSent = FILES.loadline(FILENAME_CURRENT_RIDE,FILENAME_CURRENT_RIDE_ROW_INDEX_RIDESENT).rstrip("\n")
    return int(rideSent)

def numberOfRides():
    numberOfRides = FILES.loadline(FILENAME_BASE,FILENAME_BASE_ROW_NUMBEROFRIDES)
    return int(numberOfRides)

def resetBaseFile():
    data = "0"
    FILES.save(FILENAME_BASE,data)