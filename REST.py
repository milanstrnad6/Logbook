import requests
import TIMES
import POINTS

def updateBase(lastLocation):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/base.json'
	jsonData = {"lastLocation": lastLocation}

	x = requests.patch(url, json=jsonData)

def sendLocations(rideId, part, timestamp, locationsArray):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/locations/' + rideId + '/' + 'part' + str(part) + '.json'
	jsonData = {timestamp: locationsArray}

	x = requests.patch(url, json=jsonData)

def updateRideLastLocation(year, month, week, day, rideId, lastLocation):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/rides/' + year + '/' + month + '/' + week + '/' + day + '/' + rideId + '.json'
	jsonData = {"lastLocation": lastLocation}

	x = requests.patch(url, json=jsonData)

def createRide(year, month, week, day, rideId):
	ride = {"startAddress": "", "lastAddress": "", "lastTime": "", "totalDistance": 0}

	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/rides/' + year + '/' + month + '/' + week + '/' + day + '.json'
	jsonData = {rideId: ride}

	x = requests.patch(url, json=jsonData)

def sendPoints(pointsString):
	justDateString = TIMES.justDateAsString()
	dateAsString = TIMES.nowAsString()

	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/points/' + justDateString + '.json'
	jsonData = {dateAsString: pointsString}

	x = requests.patch(url, json=jsonData)

def sendPoint(north,east):
	dateString = TIMES.justDateAsString()
	point = POINTS.getPointString(north,east)

	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/days.json'
	jsonData = {dateString: point}

	x = requests.patch(url, json=jsonData)
	#print(x.text)
