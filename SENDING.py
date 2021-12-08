import REST
import POINTS
import time

def start:
	while True:
		time.sleep(3)
		buffer = POINTS.load_allEvents()
		POINTS.reset()
		REST.sendPoints(buffer)
