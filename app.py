from flask import Flask, render_template, jsonify, Blueprint
from flask_login import LoginManager, login_required, current_user
from config import Config
from models import db, User, DroneStatus
from auth import auth as auth_blueprint
import random
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    # Récupérer les dernières données simulées
    status = DroneStatus.query.order_by(DroneStatus.timestamp.desc()).first()
    return render_template('dashboard.html', status=status, user=current_user)

@main.route('/api/telemetry')
@login_required
def get_telemetry():
    # Simuler des données en temps réel pour le dashboard
    data = {
        "battery": random.randint(70, 95),
        "speed": round(random.uniform(2.5, 5.0), 1),
        "temp": round(random.uniform(22.0, 26.0), 1),
        "depth": round(random.uniform(10.0, 50.0), 1),
        "lat": 43.2965 + random.uniform(-0.001, 0.001),
        "lng": 5.3698 + random.uniform(-0.001, 0.001)
    }
    return jsonify(data)

app.register_blueprint(auth_blueprint)
app.register_blueprint(main)

def init_db():
    with app.app_context():
        db.create_all()
        # Créer un utilisateur admin par défaut si nécessaire
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@usv.com', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            
        # Ajouter une donnée initiale
        if not DroneStatus.query.first():
            initial_status = DroneStatus(
                status="Online",
                mode="Autonomous",
                mission_status="Mapping Area A",
                uptime=3600,
                lat=43.2965,
                lng=5.3698,
                speed=3.2,
                heading=145.0,
                battery_pct=85,
                battery_voltage=24.2,
                power_consumption=120.5,
                temp_internal=28.5,
                water_temp=19.2,
                ph=8.1,
                turbidity=2.5,
                conductivity=45.0,
                oxygen=7.8,
                salinity=35.2,
                air_temp=22.5,
                humidity=65.0,
                pressure=1013.2,
                wind_speed=12.5,
                depth=25.4
            )
            db.session.add(initial_status)
        db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
