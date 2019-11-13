import requests
import bs4

response = requests.get("https://pl.wiktionary.org/wiki/Indeks:Angielski_-_Jedzenie")
# print(res.text)
soup = bs4.BeautifulSoup(response.text, "lxml")
parsedObject = soup.select("title")

for i in soup.select('.mw-headline'):
    print(i.text)

 