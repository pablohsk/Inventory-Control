from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

if __name__ == '_main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)