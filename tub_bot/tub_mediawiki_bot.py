import pywikibot
import requests
from pywikibot import family, pagegenerators, BaseSite
import urllib.parse

class Family(family.Family): 

    name = 'tub'
    langs = {
        'en-gb': '10.164.39.147:8080',
    }

    def scriptpath(self, code):
        return {
            'en-gb': '/tub',
        }[code]

    def protocol(self, code):
        return {
            'en-gb': 'http',
        }[code]


site = pywikibot.Site('en-gb', Family())

def searchAuthor(query:str, filter:str):
    if query == "null" or "Unkown":
        return
    query = 'intitle:"' + query + '"'+ filter
    pages = site.search(query)
    if all(False for _ in pages):
        print('No results found in TUB')
    result = ""
    for page in pages:
        page = pywikibot.Page(site, page.title())
        result +=page.title() + "\n" + page.text + "\n"
        ask = urllib.parse.quote("[[Category:Title]][[Has author(s)::{}]]|sort=Sort title".format(page.title()))
        url = "http://10.164.39.147:8080/tub/api.php?action=ask&format=json&query="+ ask
        response = requests.get(url).json()
        books = "Works: \n"
        for _, value in response["query"]["results"].items():
            books += value["fulltext"] + "\n"
        result = result + books + "\n\n"
    print(result)
    return result

def searchTitle(query):
    query = 'intitle:"' + query + '" incategory:"Edited title"'
    pages = site.search(query)
    result = ""
    for page in pages:
        page = pywikibot.Page(site, page.title())
        result +=page.title() + "\n" + page.text + "\n\n"
    return result