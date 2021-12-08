import requests
import TIMES
import POINTS

def sendPoints(pointsString):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/points.json'
	dateString = TIMES.justDateAsString()
	jsonData = {dateString: pointsString}

	x = requests.patch(url, json=jsonData)

def sendPoint(north,east):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/days.json'

	dateString = TIMES.justDateAsString()
	point = POINTS.getPointString(north,east)
	jsonData = {dateString: point}

	x = requests.patch(url, json=jsonData)
	#print(x.text)
