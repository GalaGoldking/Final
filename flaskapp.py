from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

with app.app_context():
    db.init_app(app)


app.config['SECRET_KEY'] = 'SECRETNIY KEIY'