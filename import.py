from flask import Flask, request
from models import *
from create import *
from sqlalchemy.sql import text

def importFlight():
    flight = Flight(origin="SG", destination="ENG", duration=10)
    db.session.add(flight)
    db.session.commit()

@app.route('/import')
def ip1():
    importFlight()
    return "Hello world"

@app.route('/text')
def text1():
    sql = text('select origin from Flights')
    result = db.engine.execute(sql)

    for row in result:
        print(row[0])
    return "Done!"