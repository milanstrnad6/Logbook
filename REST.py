import requests
import TIMES
import POINTS
import LOGGER

def updateBase(numberOfRides, lastRideKey, lastRideUrlPath):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/base.json'
	jsonData = {"numberOfRides": numberOfRides, "lastRideKey": lastRideKey, "lastRideUrlPath": lastRideUrlPath}
	response = requests.patch(url, json=jsonData)

def sendCurrentRide(rideUrlPath,rideKey):
	ride = {"totalDistance": 0}
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/rides/' + rideUrlPath + '.json'
	jsonData = {rideKey: ride}
	x = requests.patch(url, json=jsonData)
	statusCode = x.status_code
	if statusCode == 200:
		LOGGER.setRideSent(1)

def sendFirstLocation(rideUrlPath, rideKey, firstLocation):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/rides/' + rideUrlPath + '/' + rideKey + '.json'
	jsonData = {"firstLocation": firstLocation}
	x = requests.patch(url, json=jsonData)
	statusCode = x.status_code

def sendLocations(rideKey, part, timestamp, locationsArray):
	print("SEND LOCATIONS...")
	print(rideKey)
	print(part)
	print(timestamp)
	print(locationsArray)
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/locations/' + rideKey + '/' + 'part1' + '.json'
	jsonData = {timestamp: locationsArray}
	x = requests.patch(url, json=jsonData)