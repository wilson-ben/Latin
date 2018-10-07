import inflect
import requests
from bs4 import BeautifulSoup
# Pull from www.thelatinlibrary.com/decl.html
# https://en.wiktionary.org/wiki/Category:Latin_appendices

# Not currently working.

def declenFunc():
    dec_choice = input("Declension Number [1-5] : ")
    if int(dec_choice) <= 5:
        inflect_tool = inflect.engine()
        webAddr = inflect_tool.number_to_words(int(dec_choice))
        page = requests.get("https://en.wiktionary.org/wiki/Appendix:Latin_{}_declension".format(webAddr))
        entire_page = BeautifulSoup(page.text, 'html.parser')
        print(entire_page)
    elif dec_choice == '/back':
        return 0
    else:
        print("invalid choice...")
