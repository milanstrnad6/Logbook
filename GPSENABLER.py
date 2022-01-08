import RPi.GPIO as IO

GPS_START_PIN = 4

def enable():
	IO.setmode(IO.BCM)
	IO.setwarnings(0)
	IO.setup(GPS_START_PIN, IO.OUT)
	IO.output(GPS_START_PIN, 0)
    