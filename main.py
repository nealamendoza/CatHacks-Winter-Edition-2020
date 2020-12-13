import requests
from flask import Flask, render_template, flash, request
#from functions import *
#from webscraper import *
app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
def home():
    return render_template('index.html')

@app.route('/scan' , methods = ['GET' , 'POST'])
def scan():
    return render_template('verify.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
