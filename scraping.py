import requests
from bs4 import BeautifulSoup

def findreplst(url):
    html = requests.get(url)
    html_docs = html.content
    soup = BeautifulSoup(html_docs, 'html.parser')
    table = soup.find(id="votingmembers")
    pref = "https://en.wikipedia.org"

    trs = table.find("tbody").find_all("tr")[1:]
    replinks = []
    for r in trs:
        p = r.find("b")
        if(p):
            replinks.append(pref + p.find("a").get("href"))

    return replinks
