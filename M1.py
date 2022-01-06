import time
import FILES
import TIMES
import REST
import geopy.distance

###
FILENAME_CURRENT_RIDE = 'currentRide.txt'
currentRideId = "currentRide:" + TIMES.nowAsString()
FILES.saveline(FILENAME_CURRENT_RIDE,0,currentRideId)
currentRideData = FILES.load(FILENAME_CURRENT_RIDE)
print(currentRideData)

###
year = str(TIMES.currentYear())
month = str(TIMES.currentMonth())
week = str(TIMES.currentWeek())
day = str(TIMES.currentDay())
#rideId = TIMES.nowAsString()
rideId = "2021-12-28 14:00:00"
REST.createRide(year, month, week, day, rideId)

###
coord1 = (52.2296756, 21.0122287)
coord2 = (52.406374, 16.9251681)

result = geopy.distance.geodesic(coord1, coord2)
print(result.m)

###
cycle = 0
cycleDuration = 10
numberOfLocationsInPart = 0
numberOfLocationsInPartLimit = 20
part = 1

while True:
        cycle = cycle + 1
        print(cycle)

        numberOfLocationsInPart = numberOfLocationsInPart + 1
        if numberOfLocationsInPart >= numberOfLocationsInPartLimit:
                part = part + 1
                numberOfLocationsInPart = 0

        if cycle % cycleDuration == 0:
                timestamp = TIMES.nowAsString()
                locationsArray = ["N49.1797431167|E16.60379195|2021-12-17 16:54:04", "N49.1797431167|E16.60379195|2021-12-17 16:54:04", "N49.1797431167|E16.60379195|2021-12-17 16:54:04", "N49.1797431167|E16.60379195|2021-12-17 16:54:04"]
                REST.sendLocations(rideId, part, timestamp, locationsArray)
                lastLocation = "N49.1797431167|E16.60379195|2021-12-17 16:54:04 xx" + TIMES.nowAsString()
                REST.updateRideLastLocation(year, month, week, day, rideId, lastLocation)

                REST.updateBase(lastLocation)

        time.sleep(1)






