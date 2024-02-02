
from flask import Flask, render_template as rt, request

app=Flask(__name__)



@app.route('/')
def homepage():
    return rt('index.html')



app.run( debug=True )