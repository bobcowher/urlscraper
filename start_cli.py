#!/bin/python3
import time
import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

        


def getUrl(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html5lib')
    text = soup.get_text(strip = True)
    return text

def getTextPurpose(text):
    tokens = [t for t in text.split()]
    sr= stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stopwords.words('english'):
            
            clean_tokens.remove(token)
    freq = nltk.FreqDist(clean_tokens)
    # for key,val in freq.items():
    #     print(str(key) + ':' + str(val))
    freq.plot(3, cumulative=False)

def getWordFromInput(text, place):
    return text.split()[place-1]

while(True):
    userInput = input(">")
    time.sleep(1)
    print(str(userInput))

    if(userInput == "exit"):
        exit()
    elif(userInput.startswith("get url")):
        getTextPurpose(getUrl(getWordFromInput(userInput, 3)))