import REST
import POINTS
import time

def start():
        while True:
                try:
                        print "REST SLEEP FOR 10s"
                        time.sleep(10)
                        buffer = POINTS.load_allEvents()
                        POINTS.reset()
                        print "REST SEND..."
                        REST.sendPoints(buffer)
                except:
                        time.sleep(10)
                        continue
