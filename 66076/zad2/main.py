import io
import os
from urllib.request import urlopen

import bs4 as soup
import jsons


def main():
    input = getInput()
    for url in input:
        scrap(url)

def getInput():
    # TODO: odczytac input z pliku
    input = []
    input.append("https://pl.wiktionary.org/wiki/Indeks:Angielski_-_Jedzenie")
    return input

def scrap(url):
    response = urlopen(url)
    bsObj = bsObj = soup.BeautifulSoup(response.read(), 'lxml')
    model = Model()
    model.language1 = "polski"
    model.language2 = "angielski"
    with io.open(createFileName(bsObj.head.title.getText()), 'w+', encoding='utf-8') as openedFile:
        for tableRow in bsObj.find_all('tr'):
            word = getWord(tableRow)
            model.words.append(word)
        openedFile.write(jsons.dumps(model))

def createFileName(string):
    # File name can't contain: \ / * ? < > | & 
    # Let's convert those chars for _ 
    # File name can't be longer that 260 on windows (i think) but lets cut it to 50 chars to make it more beautiful
    outputFileName = string.replace("\\", "_").replace("/", "_").replace("*", "_").replace("?", "_").replace("<", "_").replace(">", "_").replace("|", "_").replace(":", "_").replace("&", "_")
    outputFileName = outputFileName[:50]
    current_work_directory = os.getcwd()
    return "./output/" + outputFileName + ".json"

def getWord(tableRow):
    word = Word()
    cells = tableRow.find_all('td')
    if (len(cells) == 0):
        return Word()
    if (len(cells) == 3):  # with photo
        word.language1 = cells[0].getText()
        word.language2 = cells[2].getText()
        img = cells[1].find_all('img')
        if (len(img) > 0):
            href = img[0]['srcset']
            word.photo = href
        else:
            word.photo = 'dupa'
        return word
    if (len(cells) == 2):
        word.language1 = cells[0].getText()
        word.language2 = cells[1].getText()
        word.photo = "null"
        return word

class Model:
    language1 = ""
    language2 = ""
    words = []


class Word:
    language1 = ""
    language2 = ""
    photo = "null"


main()

