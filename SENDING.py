import REST
import POINTS
import time
import LOGGER
import TIMES
import geopy.distance

def start():
        cyclesForPart = 360 # 360 = 360*10 seconds = 3600 seconds = 60 minutes = 1 hour
        part = 1
        cycle = 0

        while True:
                try:
                        time.sleep(10)

                        cycle = cycle + 1
                        if cycle >= cyclesForPart:
                                cycle = 0
                                #part = part + 1

                        rideUrlPath = LOGGER.rideUrlPath()
                        rideKey = LOGGER.rideKey()

                        rideSent = LOGGER.rideSent()
                        if rideSent == 0:                                
                                REST.sendCurrentRide(rideUrlPath,rideKey)
                                numberOfRides = LOGGER.numberOfRides()
                                REST.updateBase(numberOfRides, rideKey, rideUrlPath)

                        buffer = POINTS.load_allEvents()
                        bufferLength = len(buffer)
                        if bufferLength >= 1:
                                firstLocationSent = LOGGER.firstLocationSent()
                                if firstLocationSent == 0:
                                        firstLocation = buffer[0]
                                        REST.sendFirstLocation(rideUrlPath, rideKey, firstLocation)
                                        LOGGER.setFirstLocationSent(1)

                                timestamp = TIMES.nowAsString()
                                POINTS.reset()
                                rideKey = LOGGER.rideKey()
                                REST.sendLocations(rideKey, 1, timestamp, buffer)

                                distance = LOGGER.distance()
                                REST.updateDistance(rideUrlPath, rideKey, distance)
                except:
                        time.sleep(10)
                        continue
