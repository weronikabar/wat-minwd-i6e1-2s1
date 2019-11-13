from urllib.request import urlopen
import bs4 as soup
import io

def getInput():
    # TODO: odczytac input z pliku
    input = []
    input.append("https://pl.wiktionary.org/wiki/Indeks:Angielski_-_Jedzenie")
    return input

def scrap(url):
    response = urlopen(url)
    bsObj = bsObj = soup.BeautifulSoup(response.read(), 'lxml')
    with io.open("filename", 'w', encoding='utf-8') as openedFile:
        for tableRow in bsObj.find_all('tr'): 
            openedFile.write(tableRow.get_text())


def main():
    input = getInput()
    for url in input:
        scrap(url)


main()

