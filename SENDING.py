import REST
import POINTS
import time

def start():
	print "SENDING START"
	while True:
		try:
			print("SENDING SLEEP")
			time.sleep(3)
			buffer = POINTS.load_allEvents()
			POINTS.reset()
			print("SENDING SEND")
			REST.sendPoints(buffer)
		except:
			time.sleep(5)
			continue
