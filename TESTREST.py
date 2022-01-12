import requests

def send():
	url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/test.json'
	jsonData = {"testKey": "testValue"}
	x = requests.patch(url, json=jsonData)