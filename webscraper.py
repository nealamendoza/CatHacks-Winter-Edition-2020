import bs4
import requests
import lxml
import json
import re
from pprint import pprint
#from better_profanity import profanity

#dirty_text = "How is it going bitch"
#if profanity.contains_profanity(dirty_text):
    #print("Contains profanity")
#else:
    #print("This website is safe")

def data(url):
    # list of abusive words
    info = requests.get("https://www.cs.cmu.edu/~biglou/resources/bad-words.txt")
    soup = bs4.BeautifulSoup(info.text, "lxml")
    abusive_words = []
    abusive_words = soup.text.split()
    #print(abusive_words)

    # data from the website we will scrape 
    info_url = requests.get(url)
    soup_url = bs4.BeautifulSoup(info_url.text, "lxml")
    my_data = []
    my_data = soup_url.text.split()
    #print(my_data)

    count = 0
    mal_words = []
    for word in range(len(my_data)):
        for abusive_word in range(len(abusive_words)):
            if my_data[word] == abusive_words[abusive_word]:
                mal_words.append(abusive_words[abusive_word])
                count += 1
    if count == 0:
        return "this website is safe"
    else:
        return f"contains {count} malicious words"

    #return [count, mal_words]



    
print(data("https://www.dictionary.com/browse/beauty"))
#data("https://www.dictionary.com/browse/fuck")
