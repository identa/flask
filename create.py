from flask import Flask, request, jsonify
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/spring"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        main()


@app.route('/')
def hello_world():
    main()
    return "Hello world"