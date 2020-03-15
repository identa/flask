from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(45), nullable=False)
    destination = db.Column(db.String(45), nullable=False)
    duration = db.Column(db.String(45), nullable=False)