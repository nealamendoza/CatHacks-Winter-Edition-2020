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
    if profanity.contains_profanity(data):
        #profane_text = profanity.censor(my_data)
        return "Not for kids"
    else:
        return "kids, here you go"
   
print(profanity_check("https://www.commonsensemedia.org/lists/kid-safe-browsers-and-search-sites"))
#data("https://www.dictionary.com/browse/fuck")