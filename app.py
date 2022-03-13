from Flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

##  module currently running in flask (flask instance)
app = Flask(__name__)

##  Need to configure Flask to connect to Postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432'
#app.config.from_object(os.environ['APP_SETTINGS'])
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

##  Pass app into following asqlA function to create db
db = SQLAlchemy(app)

##  ??
#SQLALCHEMY_TRACK_MODIFICATIONS = True

##  create model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init_(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


##  application that serves your website - file that creates flask app
#print(__name__)

## first route - home
@app.route('/')
def home():
    #returns page from template just created
    # Nick is accessed jinja
    return render_template('home.html', name='Nick')

## Second route
@app.route('/about')
def about():
    # returns text url shortener
    return 'This is a URL shortener'

## Third route
#@app.route('/tables')
#def tables(db.Model):
#    return 0


