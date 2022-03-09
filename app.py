from flask import Flask, render_template

#1) application that serves your website - file that creates flask app

#module currently running in flask
app = Flask(__name__)

#print(__name__)

# first route
@app.route('/')

def home():
    #returns page from template just created
    # Nick is accessed jinja
    return render_template('home.html', name='Nick')

# Second route
@app.route('/about')

def about():
    # returns text url shortener
    return 'This is a URL shortener'


