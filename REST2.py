import requests

url = 'https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/users.json'
myobj = {'someKey': 'someValue'}

x = requests.post(url, data = myobj)

print(x.text)