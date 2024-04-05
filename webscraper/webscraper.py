import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        file = open("strony.txt", "w")
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                #print("\n" + url)
                resp = url + "\n"
                file.write(resp)
        file.close()
news = "https://interia.pl"
Scraper(news).scrape()






