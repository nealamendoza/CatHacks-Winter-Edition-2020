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
