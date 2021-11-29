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
email_url = 'http://fmptestuje.pl/?expugna76@fmptestuje.pl'

# wszystko musi być w funkcjach, poniewaź, importowany plik do main_code się wykonuje przy starcie
# bazujemy na wywołaniach


def name_mail():
    global email
    global email_url
    pytanie = requests.get(_url)
    print("Dane mailowe: \n")
    print(pytanie.url)
    print(re.findall('\?([^ ]*)', pytanie.url))
    email_url = pytanie.url
    email = re.findall('\?([^ ]*)', pytanie.url)
    return email[0]

def rejestracja():
    rejestracja = requests.get(email_url)
    #rejestracja_1 = BeautifulSoup(rejestracja.text, "lxml")
    rejestracja_1 = BeautifulSoup(rejestracja.text, "html.parser")
    #print(rejestracja_1)
    # rejestracja_2 = rejestracja_1.body.find('div', {'id': 'email-list'})
    # print(rejestracja_2)
    # rejestracja_2 = rejestracja_1.body.find_all('a', {'href'})
    # print(rejestracja_2)
    # rejestracja_3 = rejestracja_2.find_all('href')
    # print(rejestracja_3)
    #print(rejestracja_1.prettify())
    for link in rejestracja_1.find_all('a'):
        print(link.get('href'))

    print("=======================")
    for dane in rejestracja_1.find_all('main'):
        print(dane.get_text())










#print(re.findall('^?\S+@\S+', pytanie.url))
#print(re.findall('^?.@\\S', pytanie.url))
#print(re.findall('\?.+l', pytanie.url))
#print(re.findall('\?([^ ]*).+l', pytanie.url))
