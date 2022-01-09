import FILES

FILENAME_DEBUG = '/home/pi/Desktop/Logbook4/Logbook/debug.txt'

def log(text):
    FILES.append(FILENAME_DEBUG,text)