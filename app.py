
from flask import Flask, render_template as rt, request

app=Flask(__name__)



@app.route('/')
def homepage():
    return rt('index.html')

@app.route('/podcast')
def podcast():
    return rt('podcast.html')

@app.route('/login')
def login():
    return rt('login.html')

@app.route('/update')
def update():
    return rt('update.html')

@app.route('/aboutus')
def aboutus():
    return rt('aboutus.html')

app.run( debug=True )