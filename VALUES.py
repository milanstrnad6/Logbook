import TIMES

def rideUrlPath():
    year = str(TIMES.currentYear())
    month = str(TIMES.currentMonth())
    week = str(TIMES.currentWeek())
    day = str(TIMES.currentDay())
    return year + '/' + month + '/' + week + '/' + day

def rideKey():
    return TIMES.nowAsString()
