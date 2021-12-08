#MANAGER:HISTORY

import FILES
import TIMES

#PROPERTIES

FILENAME = '/home/pi/Desktop/Logbook2/Logbook/points.txt'

#ACTIONS: LOAD

def load_allEvents():
    return FILES.load(FILENAME)

def getPointString(north,east):
    return "N" + north + "|" + "E" + east + "|" + TIMES.stringFrom(TIMES.now()) + "\n"

#ACTIONS: SAVE

def savePoint(north,east):
    data = FILES.load(FILENAME)
    point = getPointString(north,east)
    data.append(point)
    FILES.save(FILENAME,data)

def reset():
    data = 'POINTS\n'
    FILES.save(FILENAME,data)