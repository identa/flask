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

@app.route('/getall')
def getall():
    sql = text('select * from flights')
    results = db.engine.execute(sql)

    resp = jsonify(
        {
            'result': [dict(result) for result in results]
        }
    )
    return resp

@app.route('/getfirst')
def getfirst():
    sql = text('select * from flights')
    result = db.engine.execute(sql).first()

    resp = jsonify(dict(result))
    return resp

@app.route('/getspec')
def getspec():
    sql = text('select destination, origin from flights')
    results = db.engine.execute(sql)

    resp = jsonify(
        {
            'result': [dict(result) for result in results]
        }
    )
    return resp


@app.route('/insert')
def insert():
    sql = text("insert into flights (destination, origin, duration) values ('a','b', 'c')")
    results = db.engine.execute(sql)

    print(results.lastrowid)

    resp = jsonify(
        {
            'result': results.lastrowid
        }
    )
    return resp


@app.route('/update')
def update():
    sql = text("update flights set destination = 'a', origin = 'sadasd' where destination = 'a'")
    results = db.engine.execute(sql)

    print(results.rowcount)
    resp = jsonify(
        {
            'result': results.rowcount
        }
    )
    return resp