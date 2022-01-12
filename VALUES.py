import TIMES

def rideUrlPath():
    year = str(TIMES.currentYear())
    month = str(TIMES.currentMonth())
    day = str(TIMES.currentDay())
    return year + '/' + month + '/' + day

def rideKey():
    return rideUrlPath() + '|' + TIMES.nowAsString()
