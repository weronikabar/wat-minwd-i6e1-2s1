from urllib.request import urlopen
import bs4 as soup

response = urlopen("https://pl.wiktionary.org/wiki/Indeks:Angielski_-_Jedzenie")

bsObj = soup.BeautifulSoup(response.read(), 'lxml')
file = open('output.txt', 'w')

for tableRow in bsObj.find_all('tr'): 
    file.write(tableRow.get_text())

file.close()