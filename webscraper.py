import bs4, requests, lxml
import json
import re
from pprint import pprint
from better_profanity import profanity

def profanity_check(url):
    # data from the website we will scrape
    info = requests.get(url)
    soup = bs4.BeautifulSoup(info.text, "lxml")
    my_data = ""
    my_data += soup.text
    data = my_data.split()
    #print(data[0])

    #pprint(my_data)
    words = 0
    for i in range(len(data)):
        #words = 0
        if profanity.contains_profanity(data[i]):
        #profane_text = profanity.censor(my_data)
            print(data[i])
            words += 1
    return words
    

print(profanity_check("https://www.dictionary.com/browse/fuck"))
