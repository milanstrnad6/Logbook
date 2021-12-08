#SUBMODULE:TIMES

import datetime

#PROPERTIES

FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT2 = "%Y-%m-%d"

#ACTIONS

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
