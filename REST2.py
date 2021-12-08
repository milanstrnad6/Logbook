import requests

url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)