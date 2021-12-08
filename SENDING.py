import REST
import POINTS
import time

def start():
	print "REST – START"
	while True:
		try:
			sleeptime = 10
			print "REST – SLEEP FOR ", sleeptime
			time.sleep(sleeptime)
			buffer = POINTS.load_allEvents()
			POINTS.reset()
			print("REST – SEND...")
			REST.sendPoints(buffer)
		except:
			time.sleep(10)
			continue
