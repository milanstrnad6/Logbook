import RPi.GPIO as IO

#PROPERTIES

GPS_START_PIN = 4

#SETUP

IO.setmode(IO.BCM)
IO.setwarnings(0)
IO.setup(GPS_START_PIN, IO.OUT)
IO.output(GPS_START_PIN, 1)
    