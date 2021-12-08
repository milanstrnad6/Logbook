import requests
import TIMES

url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/users.json'

date = TIMES.now()
dateString = TIMES.stringFrom(date)

jsonData = {"dateString": 'POINTS'}

#SEND REQUEST
x = requests.put(url, json=jsonData)
print(x.text)