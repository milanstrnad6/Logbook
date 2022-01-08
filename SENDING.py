import REST
import POINTS
import time
import LOGGER
import TIMES

def start():
        rideKey = LOGGER.rideKey()

        cyclesForPart = 360 # 360 = 360*10 seconds = 3600 seconds = 60 minutes = 1 hour
        part = 1
        cycle = 0

        while True:
                try:
                        time.sleep(10)
                        cycle = cycle + 1
                        if cyclesForPart >= cycle:
                                cycle = 0
                                part = part + 1

                        rideSent = LOGGER.rideSent()
                        if rideSent == 0:
                                rideUrlPath = LOGGER.rideUrlPath()
                                print("SEND CURRENT RIDE...")
                                REST.sendCurrentRide(rideUrlPath,rideKey)
                                numberOfRides = LOGGER.numberOfRides()
                                print("UPDATE BASE...")
                                REST.updateBase(numberOfRides, rideKey, rideUrlPath)

                        buffer = POINTS.load_allEvents()
                        timestamp = TIMES.nowAsString()
                        POINTS.reset()
                        REST.sendLocations(rideKey, part, timestamp, buffer)
                except:
                        time.sleep(10)
                        continue

def testSend(rideKey,part):
        buffer = POINTS.load_allEvents()
        timestamp = TIMES.nowAsString()
        POINTS.reset()
        REST.sendLocations(rideKey, part, timestamp, buffer)
