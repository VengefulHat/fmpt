# zobaczymy jak to zadziała
# już to raz zrobiłem i wsyzło nieźle ale potem się pogubiłem bo za dużo było opcji
# 3eba zoptymalizować to
import time


def rejestracja(title, data):
    # wywołanie w przypadku podaniu danych(?)
    with open('logfile.txt', 'a') as f:
        f.write("| " + time.ctime() + " | " + title)
        f.write(data)
        f.close()
    return

def asercja():
    # tutaj sprawdzamy krok pokroku (prawie)
    pass

def error(title, url):
    with open('logfile.txt', 'a') as f:
        f.write('Ten wpis oznacza wystapienie błędu, poniżej strona i nazwa karty, wykonano'
                'zrzut ekranu z nazwą URL i datą zdarzenia')
        f.write("| " + time.ctime() + " | " + title)
        f.write("| " + time.ctime() + " | " + url)
        f.close()
    return