#!/bin/python3
import time
import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
        


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

    # for key,val in freq.items():
    #     print(str(key) + ':' + str(val))
    fig = plt.figure(figsize = (10,4))
    plt.gcf().subplots_adjust(bottom=0.15) # to avoid x-ticks cut-off
    fdist = nltk.FreqDist(clean_tokens)
    fdist.plot(10, cumulative=False)
    plt.show()
    fig.savefig('plot.png', bbox_inches = "tight")
