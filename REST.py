import requests
import TIMES
import POINTS

def sendPoint(north,east):
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/days.json'

	dateString = TIMES.stringFrom(TIMES.now())
	point = POINTS.getPointString(north,east)
	jsonData = {dateString: point}

	x = requests.patch(url, json=jsonData)
	#print(x.text)
