from flask import Flask, request
from models import *
from create import *
from sqlalchemy.sql import text

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/spring"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

def importFlight():
    flight = Flight(origin="SG", destination="ENG", duration=10)
    db.session.add(flight)
    db.session.commit()


# if __name__ == '__main__':
#     with app.app_context():
#         importFlight()


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