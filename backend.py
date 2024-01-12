from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
severID = environ.get('SERVER_ID')

# connect to Database Module
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)

    def json(self):
        return {'id': self.id,'title': self.title, 'author': self.author}

with app.app_context():
    db.create_all()

#create a test route
@app.route('/test', methods=['GET'])
def test():
    return f"Hello from Book Service, server {severID}"