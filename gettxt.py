# # from bs4 import BeautifulSoup
# # import urllib2
# # link = 'https://www.thebetterindia.com/169006/dinosaur-discovery-india-rajasaurus-fossil-history/'#link from which we want to scrape the html
# # page = urllib2.urlopen(link)
# # print page
# # soup=BeautifulSoup(page)
# # # for hit in soup.findAll(attrs={'class' : ''}):
# # #     print hit.text
# # print soup.p.text
# from bs4 import BeautifulSoup
# from urllib2 import urlopen
#
# BASE_URL = "https://www.thebetterindia.com/169006/dinosaur-discovery-india-rajasaurus-fossil-history/"
#
# def get_category_links(section_url):
#     html = urlopen(section_url).read()
#     soup = BeautifulSoup(html, "lxml")
#     print soup.findAll('p')
#
# get_category_links(BASE_URL)
from lxml.html import fromstring
from lxml.html.clean import Cleaner
import requests

url = "https://www.thebetterindia.com/169006/dinosaur-discovery-india-rajasaurus-fossil-history/"
html = requests.get(url).text

doc = fromstring(html)

tags = ['h1','h2','h3','h4','h5','h6',
       'div', 'span',
       'img', 'area', 'map']
args = {'meta':False, 'safe_attrs_only':False, 'page_structure':False,
       'scripts':True, 'style':True, 'links':True, 'remove_tags':tags}
cleaner = Cleaner(**args)

path = '/html/body'
body = doc.xpath(path)[0]

print cleaner.clean_html(body).text_content().encode('ascii', 'ignore')
