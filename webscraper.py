import bs4, requests, lxml
import json
import re
from pprint import pprint
from better_profanity import profanity

#FUNC: Checks if URL is safe for Children

def profanity_check(url):
    # data from the website we will scrape
    info = requests.get(url)
    soup = bs4.BeautifulSoup(info.text, "lxml")
    my_data = ""
    my_data += soup.text
    data = my_data.split()
    for i in range(len(data)):
        if(profanity.contains_profanity(data[i])):
            return False
    return True


#Counts the Number of vulgar words in the url
def getNumOfBadWords(url):
    num_of_bad_words = 0
    info = requests.get(url)
    soup = bs4.BeautifulSoup(info.text, "lxml")
    my_data = ""
    my_data += soup.text
    data = my_data.split()
    for i in range(len(data)):
        if profanity.contains_profanity(data[i]):
            print(data[i])
            num_of_bad_words += 1

    return num_of_bad_words
