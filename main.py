import requests
from flask import Flask, render_template, flash, request
from functions import *
from webscraper import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan' , methods = ['GET' , 'POST'])
def scan():
    url = ""
    isSafe = ""
    num_of_bad_words = ""
    urlObject = {
        'url': "",
        'isSafe': "",
        'num_of_bad_words': ""
    }
    if(request.method == 'POST'):
        url = request.form['url']
        urlObject = scanWebsite(url)
        url = "Website Entered: " + urlObject['url']
        if(urlObject['isSafe'] == True):
            isSafe = "Status: Website is suitable for children to view."
        else:
            isSafe = "Status: Scanner detected vulgar language in website, it is not safe for children to view"
        if(urlObject['num_of_bad_words'] == 0):
            num_of_bad_words = "No innapropriate language was detected"
        else:
            num_of_bad_words = "Number of innapropriate words detected: " + str(urlObject['num_of_bad_words'])

    return render_template(
    'verify.html',
    url = url,
    isSafe = isSafe,
    num_of_bad_words = num_of_bad_words
    )


if __name__ == "__main__":
    app.run(debug=True)
