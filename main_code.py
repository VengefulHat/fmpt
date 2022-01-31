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
import cms.praktycznafizjoterapia as praktycznafizjoterapia
import cms.charaktery as charaktery
import cms.psychologiawpraktyce as psychologiawpraktyce
import cms.forumlogopedy as forumlogopedy

# | main code |
"""
Tu będą śmieci które jeszcze działają jako testowe (czasem)

    ### TEN KOD NIE BĘDZIE DZIAŁAŁ BO WYŁĄCZONO OPCJE ZAKUPU SYBSKRYBCJI
    # pediatriaplus.rejestracja()
    # pediatriaplus.zamowienie()
    ### TEN KOD NIE BĘDZIE DZIAŁAŁ BO WYŁĄCZONO OPCJE ZAKUPU SYBSKRYBCJI

poczta.name_mail()
    psychologiawpraktyce.rejestracja()
    psychologiawpraktyce.zamowienie()

    charaktery.rejestracja()
    charaktery.zamowienie()

    forumginekologii.rejestracja()
    forumginekologii.zamowienie()
poczta.rejestracja()
"""


if __name__ == '__main__':
    #import cnc

# CMS
#     forumlogopedy.rejestracja()
#     forumlogopedy.zamowienie()

    # psychologiawpraktyce.rejestracja()
    # psychologiawpraktyce.zamowienie()

    forumlogopedy.rejestracja()
    forumlogopedy.zamowienie()
    #
    forumginekologii.rejestracja()
    forumginekologii.zamowienie()

    charaktery.rejestracja()
    charaktery.zamowienie()

    praktycznafizjoterapia.rejestracja()
    praktycznafizjoterapia.zamowienie()


# NETFLIXY

    literkaprzedszkole.rejestracja()
    literkaprzedszkole.zamowienie()

    animalexpertplus.rejestracja()
    animalexpertplus.zamowienie()

    charakteryplus.rejestracja()
    charakteryplus.zamowienie()

    doradcaksiegowego.rejestracja()
    doradcaksiegowego.zamowienie()

    net_fiz.rejestracja()
    net_fiz.zamowienie()

    # poczta.wuef()
    # time.sleep(23456)
    pass
