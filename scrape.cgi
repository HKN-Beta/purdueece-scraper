#! /usr/bin/env python3
import os
import requests
import unicodedata
from bs4 import BeautifulSoup
import json

# URL to scrape
url = 'https://purdueece.com/'

# Get the HTML
r = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Get all article elements as a list
articles = soup.find_all('article')

# create an empty bs4 object
article_dict = []

def fixunicode(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

# For each article, get the title from the innerhtml of the anchor tag under h1.entry-title
# the author from the innerhtml of the anchor tag  under span.author
for article in articles:
    adict = {}
    adict["title"] = fixunicode(article.find('h1', class_='entry-title').a.text)
    adict["date"] = fixunicode(article.find('time', class_='entry-date').text)
    adict["author"] = fixunicode(article.find('span', class_='author').a.text)
    adict["url"] = fixunicode(article.find('h1', class_='entry-title').a['href'])
    # if there exists an img under the article's .entry-content div, grab its src attribute
    if article.find('div', class_='entry-content').img:
        adict["img"] = fixunicode(article.find('div', class_='entry-content').img['src'])
    # if there exists a div with class wp-block-pdfb-pdf-block, get the src attribute of the iframe
    if article.find('div', class_='wp-block-pdfb-pdf-block'):
        adict["pdf"] = article.find('div', class_='wp-block-pdfb-pdf-block').iframe['src']
    # otherwise if there exists paragraph elements under the article's .entry-content div, add each 
    # paragraph to a list
    if article.find('div', class_='entry-content').find_all('p'):
        paragraphs = article.find('div', class_='entry-content').find_all('p')
        adict["paragraphs"] = [fixunicode(p.text) for p in paragraphs]
    # append the object to articles
    article_dict.append(adict)

if 'REMOTE_ADDR' in os.environ:
    # we are running in CGI mode, print json header
    print("Content-Type: application/json\r\n")
print(json.dumps(article_dict, indent=4))
