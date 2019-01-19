from flask import Flask, request, render_template
app = Flask(__name__)

import urllib.request
import re
import nltk
import operator
from bs4 import BeautifulSoup
import spacy
import textacy
import requests
import json
import time
from urllib.error import HTTPError


@app.route('/')
def my_form():
    return render_template('/index.html')
processed_text=" k "
myjson={}
@app.route('/', methods=['POST'])
def my_form_post():
    flag=0
    text = request.form['text']
    global processed_text
    processed_text = text
    flag=summarize()
    time.sleep(7)
    if(flag==1):
        print("DONE")
    else:
        return ("page does not exist.try something else")
    return render_template('/profile.html',myjson=myjson,processed_text=processed_text)

    #return processed_text
    # return render_template('/profile.html')
def summarize():
    name=processed_text
    scraped_data = urllib.request.urlopen('https://en.wikipedia.org/api/rest_v1/page/html/'+processed_text)
    #
    # req = urllib.request.Request(url=r"http://borel.slu.edu/cgi-bin/cc.cgi?foirm_ionchur=im&foirm=Seol&hits=1&format=xml",headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    # try:
    #     handler = urllib.request.urlopen(req)
    # except HTTPError as e:
    #     content = e.read()
    article = scraped_data.read()

    parsed_article = BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    sentence_list = nltk.sent_tokenize(article_text)

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    maxi=""
    maxc=-1
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
                if(word_frequencies[word]>maxc):
                    maxc=word_frequencies[word]
                    maxi=word
                    maximum_frequncy = max(word_frequencies.values())
    cd = sorted(word_frequencies.items(),key=operator.itemgetter(1),reverse=True)
    l=[]
    i=1
    s=cd[0][1]
    l.append(cd[0][0])
    while(i<len(cd) and s+cd[i][1]<1000):#len
        l.append(cd[i][0])
        s+=cd[i][1]
        i+=1
    #l has buzzwords
    nlp = spacy.load('en_core_web_sm')
    ARTICLE = name #user input  in this field
    # ENDPOINT = "https://en.wikipedia.org/api/rest_v1/page/html/"
    # ENDPOINT+=ARTICLE
    # req = requests.get(ENDPOINT)
    text = parsed_article.select("body")[0].get_text().strip()
    doc = nlp(text)
    def cleanup(s):
        strip_refs = re.compile("\.?\[\d+\]?")
        s = strip_refs.sub("", s).strip()
        s=re.sub(r'\[[0-9]*\]',' ',s)
        s=re.sub(r'\s+',' ',s)
        if s[-1] == ".":
            s = s[0:-1]
        return s

    m=[]
    for i in l:
        statements = textacy.extract.semistructured_statements(doc,i)
        for statement in statements:
            subject, verb, fact = statement
            fact = cleanup(str(fact))
            if(fact.count(' ')>2):
                m.append(fact)

    global myjson
    myjson = m
    print (myjson)
    return 1

if __name__=='__main__':
    app.run(debug=True)
