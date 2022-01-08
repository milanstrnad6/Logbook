import time
import FILES
import TIMES
import REST
import geopy.distance
import LOGGER
import POINTS
import SENDING

###
POINTS.reset()
LOGGER.logNewRide()

###
coord1 = (52.2296756, 21.0122287)
coord2 = (52.406374, 16.9251681)
#result = geopy.distance.geodesic(coord1, coord2)
#print(result.m)

###
cycle = 0
cycleDuration = 5 #10
numberOfLocationsInPart = 0
numberOfLocationsInPartLimit = 20
part = 1

while True:
        cycle = cycle + 1
        print(cycle)

        rideSent = LOGGER.rideSent()
        if rideSent == 0:
                rideUrlPath = LOGGER.rideUrlPath()
                rideKey = LOGGER.rideKey()
                REST.sendCurrentRide(rideUrlPath,rideKey)
                numberOfRides = LOGGER.numberOfRides()
                REST.updateBase(numberOfRides, rideKey, rideUrlPath)

        POINTS.saveClearPoint(rideKey)

        numberOfLocationsInPart = numberOfLocationsInPart + 1
        if numberOfLocationsInPart >= numberOfLocationsInPartLimit:
                part = part + 1
                numberOfLocationsInPart = 0

        if cycle % cycleDuration == 0:
                timestamp = TIMES.nowAsString()
                locationsArray = ["N49.1797431167|E16.60379195|2021-12-17 16:54:04", "N49.1797431167|E16.60379195|2021-12-17 16:54:04", "N49.1797431167|E16.60379195|2021-12-17 16:54:04", "N49.1797431167|E16.60379195|2021-12-17 16:54:04"]
                #REST.sendLocations(rideId, part, timestamp, locationsArray)
                lastLocation = "N49.1797431167|E16.60379195|2021-12-17 16:54:04 xx" + TIMES.nowAsString()
                #REST.updateRideLastLocation(year, month, week, day, rideId, lastLocation)

                #print("UPDATE BASE")
                #REST.updateBase(lastLocation)

                SENDING.testSend(rideKey, part)

        time.sleep(1)






