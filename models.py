from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(512))
    role = db.Column(db.String(20), default='operator') # admin, operator, viewer

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class DroneStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # État général
    status = db.Column(db.String(20)) # Online, Offline
    mode = db.Column(db.String(20)) # Manual, Autonomous, RTL
    mission_status = db.Column(db.String(50))
    uptime = db.Column(db.Integer) # seconds
    
    # Navigation
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    speed = db.Column(db.Float)
    heading = db.Column(db.Float)
    
    # Énergie
    battery_pct = db.Column(db.Integer)
    battery_voltage = db.Column(db.Float)
    power_consumption = db.Column(db.Float)
    temp_internal = db.Column(db.Float)
    
    # Environnement
    water_temp = db.Column(db.Float)
    ph = db.Column(db.Float)
    turbidity = db.Column(db.Float)
    conductivity = db.Column(db.Float)
    oxygen = db.Column(db.Float)
    salinity = db.Column(db.Float)
    
    # Météo
    air_temp = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    wind_speed = db.Column(db.Float)
    
    # Bathymétrie
    depth = db.Column(db.Float)
