
import urllib
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
#from cltk.stem.latin.declension import CollatinusDecliner
#import declensions
import sys
# TODO -- All input sources connect. -- FIX FORMATTING ON VERBS --

def parseWiki(pageData):


    if 'Conjugation' in str(pageData[0]):
        print("verb")
        return tabulate(pageData[0], headers='keys', tablefmt='fancy_grid')
    elif 'Case' in str(pageData[0]):
        return tabulate(pageData[0], headers='keys', tablefmt='fancy_grid')

    else:
        print("conflict with table. Try another word?")

def getWiki(word):
    try:
        wiki_page = requests.get("https://en.wiktionary.org/w/index.php?title={}".format(str(word)))
    except:
        print("word does not have wiktionary entry...")

    soup = BeautifulSoup(wiki_page.content, 'lxml')
    table1 = ' '
    table2 = ' '
    try:
        table1 = soup.find_all('table', {"class": "inflection-table"})
    except:
        table1 = ' '
    try:
        table2 = soup.find_all('table', {"class": "inflection-table"})
    except:
        table2 = ' '
    if table1 != ' ':

        df1 = pd.read_html(str(table1))
        df = df1
        print(parseWiki(df))
    elif table2 != ' ':
          df = pd.read_html(str(table2))
          print(parseWiki(df))
    else:
        print("Error finding wiki entry")
    #entire_page = BeautifulSoup(wiki_page.text, 'html.parser')

    #return_words = entire_page.find('tbody')


#    more_info = parseWiki(return_words)
#    print(more_info)

def getEngWords(sentence):
    if ' ' not in sentence:

        try:
            page = requests.get("http://archives.nd.edu/cgi-bin/wordz.pl?english={}".format(str(sentence)))
        except:
            print("Error with word. Not valid?? ")
            main()
        entire_page = BeautifulSoup(page.text, 'html.parser')

        return_words = entire_page.find_all("pre")
        return_words = str(return_words)
        preRem = return_words.replace('[<pre>\n\n', '')
        words_list = preRem.replace('\n</pre>]', '')
        chooseWord = words_list.split('\n\n')

        for i in range(len(chooseWord)):
            print("Option {} --- {}\n ".format(i, chooseWord[i]))

        while True:
            word_choice = input("Choose Word to Recieve More info about : ")
            if word_choice != '/back':
                limiter = chooseWord[int(word_choice)]
                word = limiter.split(', ')

                getWiki(word[0])
            else:
                getWord('E')

    else:
        pass
        # Add sentence Translation later
def getLatWords(sentence):
    if ' ' not in sentence:

        try:
            page = requests.get("http://archives.nd.edu/cgi-bin/wordz.pl?keyword={}".format(str(sentence)))
        except:
            print("Error with word. Not valid?? ")
            main()
        entire_page = BeautifulSoup(page.text, 'html.parser')

        return_words = entire_page.find_all("pre")
        return_words = str(return_words)
        preRem = return_words.replace('[<pre>\n\n', '')
        nextRem = preRem.replace('[<pre>\n', '')
        words_list = nextRem.replace('\n</pre>]', '')
        rmDot = words_list.replace(".", "")
        chooseWord = rmDot.split('\n\n\n')

        for i in range(len(chooseWord)):
            print("Option {} --- {}\n ".format(i, chooseWord[i]))

        while True:
            word_choice = input("Choose Word to Recieve More info about : ")
            if word_choice != '/back':
                limiter = chooseWord[int(word_choice)]
                word = limiter.split(' ')

                getWiki(word[0])



            else:
                getWord("L")
    else:
        pass

        # Add sentence Translation later

def getWord(lat_or_eng):
    if "L" in lat_or_eng:
        userLatSentence = input("Enter a Sentence & Words to Translate : ")
        if userLatSentence != '/back':
            getLatWords(userLatSentence)
        else:
            main()
        # except
        # print("Error with Sentence ")

    elif "E" in lat_or_eng:

        userEngSentence = input("Enter a Sentence & Words to Translate : ")
        if userEngSentence != '/back':
            getEngWords(userEngSentence)
        else:
            main()
    else:
        main()
def main():
    while True:
        shell = input("Latin> ")
        if shell == "translate":
            lat_or_eng = input("Latin-to(L) or English-to(E) ")
            if 'lat_or_eng' != '/quit':
                getWord(lat_or_eng)
            else:
                sys.exit()
        elif shell == "help":
            print("""
            help : This screen right here
            translate : translate to or from Latin
            vocab : basic vocab to view and learn from
            declensions : view declensions
            conjugations : view the different conjugations
            irregular : view irregular cases
            about : more about this tool
            /quit : leave the program
            /back : move back in the structure tree
            """)
        elif shell == "declensions":
            print("not currently working")
            declensions.declenFunc()
        elif shell == "/quit":
            sys.exit()

main()
