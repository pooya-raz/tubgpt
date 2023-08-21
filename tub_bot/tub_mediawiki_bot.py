import pywikibot

from pywikibot import family, pagegenerators, BaseSite


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

def search(query, category):
    query = 'intitle:"' + query + '" incategory:"' + category + '"'
    print(query)
    pages = site.search(query)
    result = ""
    for page in pages:
        page = pywikibot.Page(site, page.title())
        result +=page.title() + "\n" + page.text + "\n\n"
    return result
print(search('Shahid', "Author"))