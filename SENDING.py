import REST
import POINTS
import time
import LOGGER
import TIMES

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
                                part = part + 1

                        rideUrlPath = LOGGER.rideUrlPath()
                        rideKey = LOGGER.rideKey()

                        rideSent = LOGGER.rideSent()
                        if rideSent == 0:                                
                                REST.sendCurrentRide(rideUrlPath,rideKey)
                                numberOfRides = LOGGER.numberOfRides()
                                REST.updateBase(numberOfRides, rideKey, rideUrlPath)

                        buffer = POINTS.load_allEvents()
                        print("BUFFER =")
                        print(buffer)
                        print("BUFFER LENGTH =")
                        bufferLength = len(buffer)
                        print(bufferLength)
                        if bufferLength >= 1:
                                firstLocationSent = LOGGER.firstLocationSent()
                                if firstLocationSent == 0:
                                        firstLocation = buffer[0]
                                        print("FIRST LOCATION =")
                                        print(firstLocation)
                                        REST.sendFirstLocation(firstLocation)
                                        LOGGER.setFirstLocationSent(1)

                                timestamp = TIMES.nowAsString()
                                POINTS.reset()
                                rideKey = LOGGER.rideKey()
                                REST.sendLocations(rideKey, part, timestamp, buffer)
                except:
                        time.sleep(10)
                        continue

def testSend(rideKey,part):
        buffer = POINTS.load_allEvents()
        timestamp = TIMES.nowAsString()
        POINTS.reset()
        REST.sendLocations(rideKey, part, timestamp, buffer)
