#SUBMODULE:TIMES

import datetime

#PROPERTIES

FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT2 = "%Y-%m-%d"

#ACTIONS

def currentYear():
	return datetime.datetime.now().year

def currentMonth():
	return datetime.datetime.now().month

def currentWeek():
	return datetime.datetime.now().isocalendar()[1]

def currentDay():
	return datetime.datetime.now().day

def justDateAsString():
	return datetime.datetime.now().strftime(FORMAT2)

def now():
	return datetime.datetime.now()

def nowAsString():
    return datetime.datetime.now().strftime(FORMAT)

def dateFrom(string):
    return datetime.datetime.strptime(string,FORMAT)

def stringFrom(date):
    return date.strftime(FORMAT)
