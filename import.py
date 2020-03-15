from flask import Flask, request
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/spring"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flight = Flight(origin="SG", destination="ENG", duration=10)
    db.session.add(flight)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        main()


@app.route('/import')
def hello_world():
    main()
    return "Hello world"