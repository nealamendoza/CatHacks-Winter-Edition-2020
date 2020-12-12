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
<<<<<<< HEAD
    data = my_data.split()
    #print(data[0])
=======


    word = ""
    list_of_words = []
    for i in range(len(soup.text)-1):
        #print(soup.text[i])
        if((soup.text[i] == ' ') and (len(word) > 0)):
            list_of_words.append(word)
            word = ""
        else:
            if(soup.text[i] + soup.text[i+1] != "\n" ):
                word += soup.text[i]


    print(list_of_words)
>>>>>>> fc81e14cd79256672ec45ce698c46dd063efe144

    #pprint(my_data)
    if profanity.contains_profanity(data):
        #profane_text = profanity.censor(my_data)
        return "Not for kids"
    else:
        return "kids, here you go"

print(profanity_check(Enter URL))
