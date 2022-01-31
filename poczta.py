# poczta, mam nadzieję że nikt juz nic nie zmieni w tej poczcie od fmptestuje.pl
# da się to zespolć w jakiś konkretny mail, nawet nie trzeba otwierać strony w przeglądarce
# wystarczy zwykły get, i mamy zwracany link URL z maili em

# import bibliotek:
import requests
import time
import re
from bs4 import BeautifulSoup


# stałe wartości
_url = 'http://fmptestuje.pl'
email = ''
email_url = ''
lista_href = []
rejestracja_url = ''

# wszystko musi być w funkcjach, poniewaź, importowany plik do main_code się wykonuje przy starcie
# bazujemy na wywołaniach


def name_mail():
    global email
    global email_url
    pytanie = requests.get(_url)
    print("Dane mailowe: \n")
    print(pytanie.url)
    print(re.findall('\?([^ ]*)', pytanie.url))
    email_url = ''
    email_url = pytanie.url
    email = re.findall('\?([^ ]*)', pytanie.url)
    return email[0]

def rejestracja():
    global rejestracja_url
    global email_url
    time.sleep(10)
    rejestracja = requests.get(email_url)
    rejestracja_1 = BeautifulSoup(rejestracja.text, "html.parser")
    for link in rejestracja_1.find_all('a'):
        lista_href.append(link.get('href'))
    for href in lista_href:
        if 'aktywacja' in str(href):
            rejestracja_url = href
    email_url = ''
    return rejestracja_url

def rejestracjaCMS():
    global rejestracja_url
    global email_url
    time.sleep(10)
    rejestracja = requests.get(email_url)
    rejestracja_1 = BeautifulSoup(rejestracja.text, "html.parser")
    for link in rejestracja_1.find_all('a'):
        lista_href.append(link.get('href'))
    for href in lista_href:
        if 'resetting' in str(href):
            rejestracja_url = href
    email_url = ''
    return rejestracja_url

def wuef():
    url = 'http://fmptestuje.pl/?kai71@fmptestuje.pl#mail-box-2404'
    praca = requests.get(url)
    pracaa = BeautifulSoup(praca.text, "html.parser")
    dana = pracaa.find_all("td", {'class': 'width-100-center'})
    dane111 = pracaa.select("td > tr:nth-of-type(3) tr:nth-of-type(3) [width]")
    print(len(dane111))
    print(len(dana))
    print(dana)
    for syntaks in dana:
        print("a")
        if "nr" in str(syntaks):
            deny = re.findall("^['<Zamówienie nr> ']")
            print(syntaks)
    pass
