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
    abs_work_directory = os.path.abspath(current_work_directory)

    return "./output/" + outputFileName

def getWord(tableRow):
    word = Word()
    word.language1 = "baleron m"
    word.language2 = "gammon"
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

