import pymongo
from keys import *
from pymongo import MongoClient
from webscraper import *


db = cluster["test"]
collection = db["test"]


def check_url_in_db(url):
    title = ""
    results = collection.find({"_id":url})
    for result in results:
        title = result['_id']
    if(title == url):
        return True
    else:
        return False


def add_url_to_db(urlObject):
    index = {
        '_id': urlObject['_id'],
        'isSafe': urlObject['isSafe'],
        'num_of_bad_words': urlObject['num_of_bad_words']
    }
    collection.insert_one(index)

def retrieve_data_from_db(url):
    urlObject = {
        'url': "",
        'isSafe': "",
        'num_of_bad_words': 0
    }
    results = collection.find({"_id":url})
    for result in results:
        urlObject['url'] = result['_id']
        urlObject['isSafe'] = result['isSafe']
        urlObject['num_of_bad_words'] = result['num_of_bad_words']
    return  urlObject

def scanWebsite(userUrl):
    url = userUrl
    condition = check_url_in_db(url)
    if(condition == True):
        print(' "status": "Already Added to Database"')
        urlObject = retrieve_data_from_db(url)
        return urlObject
    else:
        urlObject = {
            '_id': url,
            'isSafe': True,
            'num_of_bad_words': 0
        }
        isSafe = profanity_check(url)
        urlObject['isSafe'] = isSafe
        num_of_bad_words = getNumOfBadWords(url)
        urlObject['num_of_bad_words'] = num_of_bad_words
        add_url_to_db(urlObject)
        print('"status": "Created New Entry in Database"')
        return retrieve_data_from_db(url)




url = (input(""))

print(scanWebsite(url))
