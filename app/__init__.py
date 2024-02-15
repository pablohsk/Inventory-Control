from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import main_bp
app.register_blueprint(main_bp)

from app.model import Car, User, Employee, Sale, SaleCar

with app.app_context():
    db.create_all()