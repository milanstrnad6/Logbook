#MANAGER:HISTORY

import FILES
import TIMES

#PROPERTIES

FILENAME = '/home/pi/Desktop/Logbook/points.txt'

#ACTIONS: LOAD

def load_allEvents():
    return FILES.load(FILENAME)

#ACTIONS: SAVE

def savePoint(north,east):
    data = FILES.load(FILENAME)
    date = TIMES.now()
    record = "N" + north + "|" + "E" + east + "|" + TIMES.stringFrom(date) + "\n"
    data.append(record)
    FILES.save(FILENAME,data)

def reset():
    data = 'POINTS\n'
    FILES.save(FILENAME,data)