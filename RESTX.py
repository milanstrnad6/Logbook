from firebase import firebase
firebase = firebase.FirebaseApplication('https://carassistant-479b4-default-rtdb.europe-west1.firebasedatabase.app/', None)
new_user = 'raspberry'

result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result
{u'name': u'-Io26123nDHkfybDIGl7'}

result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result == None
True