import bs4
import requests
import lxml
import json
import re
from pprint import pprint
from better_profanity import profanity

'''
This function will return the number of vulgar
words in a website.
It gets a list of vulgar words from a website
and checks if any words from the webstie are in that list
'''
def getNumOfBadWords(url):
    # list of abusive words
    info = requests.get("https://www.cs.cmu.edu/~biglou/resources/bad-words.txt")
    soup = bs4.BeautifulSoup(info.text, "lxml")

    abusive_words = []
    abusive_words = soup.text.split()

    # data from the website we will scrape
    info_url = requests.get(url)
    soup_url = bs4.BeautifulSoup(info_url.text, "lxml")
    my_data = []
    my_data = soup_url.text.split()

    count = 0
    for word in range(len(my_data)):
        if(my_data[word] in abusive_words):
            count += 1
            print(my_data[word])
        #for abusive_word in range(len(abusive_words)):
            #if my_data[word] == abusive_words[abusive_word]:
            #    count += 1
            #    break

    return count


'''
This function checks if a website is safe for children
Returns True if it is safe
Returns False if the website is not safe for children
'''
def profanity_check(url):
    info = requests.get(url)
    soup = bs4.BeautifulSoup(info.text, "lxml")
    my_data = ""
    my_data += soup.text
    data = my_data.split()
    for i in range(len(data)):
        if profanity.contains_profanity(data[i]):
            return False

    return True
