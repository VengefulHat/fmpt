# ========================================= #
# z racji tego, że kod poprzedni 'rozpoznanieWEB' miał podan 25 tyś linijek w jednym pliku
# praca w nim nie sprawiała przyjemności
# na podstawie zmian jakie jakie powstały na stronach bardzo często zmiany w kodzie musiałby wystąpić w każdej sekcji
# stą wsyzstko będzie teraz dzielone po bożemu
# ========================================= #

# import bibliotek:
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




# import modułów:
import animalexpertplus
import charakteryplus
import doradcaksięgowego
import net_fiz
import pediatriaplus
import poczta
import literkaprzedszkole


# | main code |

if __name__ == '__main__':
    #poczta.name_mail()
    poczta.rejestracja()
    # literkaprzedszkole.logowanie()
    # animalexpertplus.logowanie()
    # charakteryplus.logowanie()
    # doradcaksięgowego.logowanie()
    # net_fiz.logowanie()
    # pediatriaplus.logowanie()
    pass
    # coś przewiduje że to będzie dużo pisania
    # oby moje ćwiczenia na szybkiego pisanie sie na coś przydały ;_;

#print(poczta.name_mail())
