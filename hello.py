from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
@app.route("/")
def hello():
    return "Hello World!"

# @app.route('/')
# def my_form():
#     return render_template('/form.html')
# #processed_text=''
# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text
    #return processed_text
# @app.route('/name',methods=['POST','GET'])
# def abc():
#     print("heyy")
#     return ('hh')
#     #SOURCE:https://github.com/hay/wiki-text-nlp/blob/master/wiki-text-nlp.ipynb
#     if( request.method=='POST'):
#         print ("HEY")
#         import urllib.request
#         import re
#         import nltk
#         import operator
#         from bs4 import BeautifulSoup
#         import spacy
#         import textacy
#         import requests
#         import json
#         # nltk.download('punkt')
#         # nltk.download('stopwords')
#         name="Pakistan"
#         scraped_data = urllib.request.urlopen('https://en.wikipedia.org/api/rest_v1/page/html/'+name)
#         article = scraped_data.read()
#
#         parsed_article = BeautifulSoup(article,'lxml')
#
#         paragraphs = parsed_article.find_all('p')
#
#         article_text = ""
#
#         for p in paragraphs:
#             article_text += p.text
#
#             # Removing Square Brackets and Extra Spaces
#         article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
#         article_text = re.sub(r'\s+', ' ', article_text)
#
#         # Removing special characters and digits
#         formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
#         formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
#
#
#
#         sentence_list = nltk.sent_tokenize(article_text)
#
#         stopwords = nltk.corpus.stopwords.words('english')
#
#         word_frequencies = {}
#         maxi=""
#         maxc=-1
#         for word in nltk.word_tokenize(formatted_article_text):
#             if word not in stopwords:
#                 if word not in word_frequencies.keys():
#                     word_frequencies[word] = 1
#                 else:
#                     word_frequencies[word] += 1
#                     if(word_frequencies[word]>maxc):
#                         maxc=word_frequencies[word]
#                         maxi=word
#                         maximum_frequncy = max(word_frequencies.values())
#         cd = sorted(word_frequencies.items(),key=operator.itemgetter(1),reverse=True)
#         l=[]
#         i=1
#         s=cd[0][1]
#         l.append(cd[0][0])
#         while(i<len(cd) and s+cd[i][1]<(len(parsed_article))):
#             l.append(cd[i][0])
#             s+=cd[i][1]
#             i+=1
#         #l has buzzwords
#
#
#         nlp = spacy.load('en_core_web_sm')
#         # text ="""
#         #
#         # """
#         ARTICLE = name #we'll have to take input from user in this field
#         # ENDPOINT = "https://en.wikipedia.org/api/rest_v1/page/html/"
#         # ENDPOINT+=ARTICLE
#         # req = requests.get(ENDPOINT)
#         #
#         # soup = BeautifulSoup(req.text, "lxml")
#         text = parsed_article.select("body")[0].get_text().strip()
#
#
#         doc = nlp(text)
#         # most_occuring=textacy.extract.named_entities(doc,exclude_types="NUMERIC",drop_determiners=True, min_freq=5)
#         # for i in most_occuring:
#         #     print(i)
#         # abc123=textacy.keyterms.key_terms_from_semantic_network(doc,ranking_algo='pagerank')
#         # for i in abc123:
#         #     print(i)
#         # for i in textacy.keyterms.textrank(doc, normalize='lemma'):
#         #     print (i)
#         def cleanup(s):
#             strip_refs = re.compile("\.?\[\d+\]?")
#             s = strip_refs.sub("", s).strip()
#             s=re.sub(r'\[[0-9]*\]',' ',s)
#             s=re.sub(r'\s+',' ',s)
#             if s[-1] == ".":
#                 s = s[0:-1]
#             return s
#         #print (l)
#         m=[]
#         for i in l:
#             statements = textacy.extract.semistructured_statements(doc,i)
#             for statement in statements:
#                 subject, verb, fact = statement
#                 fact = cleanup(str(fact))
#                 #print(fact)
#                 m.append(fact)
#         #print (m)
#         i= (json.dumps({ARTICLE:m}))
#         r = ((json.loads(i)))
#         #print(SUCCESS)
#         # print("Did you know this...")
#         # for statement in statements:
#         #     subject, verb, fact = statement
#         #     fact = cleanup(str(fact))
#         #     print(fact)
#         result = request.form
#         return render_template("result.html",r=r)
if __name__=='__main__':
    app.run()
# abc()
