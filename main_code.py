# ========================================= #
"""
z racji tego, że kod poprzedni 'rozpoznanieWEB' miał ponad 25 tyś linijek w jednym pliku
praca w nim nie sprawiała przyjemności
na podstawie zmian jakie jakie powstały na stronach bardzo często zmiany w kodzie musiałby wystąpić w każdej sekcji
stą wsyzstko będzie teraz dzielone po bożemu
"""
# ========================================= #

# import bibliotek:
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# import modułów:
import dane
import poczta

# - netflixy:
import netflixy.animalexpertplus as animalexpertplus
import netflixy.charakteryplus as charakteryplus
import netflixy.doradcaksięgowego as doradcaksiegowego
import netflixy.net_fiz as net_fiz
import netflixy.pediatriaplus as pediatriaplus
import netflixy.literkaprzedszkole as literkaprzedszkole

# - cms:
import cms.forumginekologii as forumginekologii


# | main code |

if __name__ == '__main__':
    # poczta.name_mail()
    # poczta.rejestracja()

    forumginekologii.rejestracja()

    # literkaprzedszkole.rejestracja()
    # literkaprzedszkole.zamowienie()
    #
    # animalexpertplus.rejestracja()
    # animalexpertplus.zamowienie()
    #
    #
    # charakteryplus.rejestracja()
    # charakteryplus.zamowienie()
    #
    #
    # doradcaksiegowego.rejestracja()
    # doradcaksiegowego.zamowienie()
    #
    #
    # net_fiz.rejestracja()
    # net_fiz.zamowienie()
    #
    # pediatriaplus.rejestracja()
    # pediatriaplus.zamowienie()

    # time.sleep(23456)
    pass

#print(poczta.name_mail())
