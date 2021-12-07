#API

from flask import request
from flask_api import FlaskAPI

import POINTS

#PROPERTIES

app = FlaskAPI(__name__)

#ENDPOINTS

@app.route('/getAllData/', methods=["GET"])
def getAllData():
    print("API - GET ALL DATA")
    if request.method == "GET":
        events = POINTS.load_allEvents()

    return {"data":{
        "events":events
    }}

#MAIN

if __name__ == "__main__":
    app.run()
