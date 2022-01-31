# import bibliotek:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# import modułów
import dane
import LogFile
import poczta


# | maine code |


def rejestracja():
    global browser
    war = 0
    help = 0
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(dane.pediatriaplus_url)
    browser.maximize_window()
    time.sleep(2)
    dane.AdTerminator(browser)
    browser.refresh()
    time.sleep(2)
    browser.find_element_by_xpath("//a[contains(text(),'Zaloguj')]").click()
    time.sleep(3)
    browser.find_element_by_xpath("//a[contains(text(),'Zarejestruj się')]").click()
    time.sleep(2)
    while war == 0:
        if browser.current_url == 'https://www.pediatriaplus.pl/rejestracja':
            war += 1
        else:
            help += 1
            # tojest potrzebne jakby ta pętla mała trwać w nieskończonośći a tak
            # to się wywali jak należy
            if help > 100000:
                browser.save_screenshot(browser.current_url + ' ' + time.ctime())
                LogFile.error(browser.title, browser.current_url)
            continue
    browser.find_element_by_id("register-email").send_keys(poczta.name_mail())
    browser.find_element_by_name("phoneNumber").send_keys(dane.Phone)
    browser.find_element_by_name("firstName").send_keys(dane.Fname)
    browser.find_element_by_name("lastName").send_keys(dane.Lname)
    browser.find_element_by_name('npwz').send_keys(dane.npwz)
    browser.execute_script("$('select#spec-multiselect')[0].sumo.selectItem('Endokrynologia_i_diabetologia_dziecięca');")
    browser.execute_script("document.getElementById('agree1').checked = true;")
    time.sleep(1)
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)
    # LogFile.logowanie()
    print("Teraz wchodzimy w link do reejstracji z mailia:")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    browser.get(poczta.rejestracja())
    time.sleep(3)
    dane.AdTerminator(browser)
    browser.find_element_by_name("password[new]").send_keys(dane.haslo)
    browser.find_element_by_name("password[new-repeat]").send_keys(dane.haslo)
    time.sleep(2)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    print("Rejestracja przebiegła poprawnie")
    time.sleep(3)
    return

### TEN KOD NIE BĘDZIE DZIAŁAŁ BO WYŁĄCZONO OPCJE ZAKUPU SYBSKRYBCJI
def zamowienie():
    #dane.cmspopupshutup(browser)
    print("przechodzimy do zamówienia, na pediatrzeplus wybierzemy pakiet z osobisty na miesiąc")
    browser.find_element_by_xpath("//a[contains(text(),'Oferta')]").click()
    time.sleep(5)
    try:
        browser.find_element_by_xpath("(//a[contains(text(),'Wybieram')])[3]").click()# na miesiąc
    except Exception as e:
        print("1.asda")
        print(e)
    try:
        browser.find_element_by_class_name(".col-12:nth-child(3) > .offer__plans_tile .btn-main").click()# na miesiąc
    except Exception as e:
        print("2.asdads")
        print(e)
    try:
        browser.find_element_by_xpath("//div[3]/div/div[4]/a").click()# na miesiąc
    except Exception as e:
        print("3.asdasdf")
        print(e)


    time.sleep(2)
    # powinno być już zazaczone ale jeszcze raz jakby randomowo się to zazcnaczało
    #browser.find_element_by_xpath("(//a[contains(@href, '/logowanie')])[2]").click()# baton do logowania
    try:
        browser.find_element_by_class_name(".nav-item--private > .nav-link-dot").click()  # na osobę prywatną
    except Exception as e:
        print(e)

    browser.find_element_by_name('npwz').send_keys(dane.npwz)
    browser.execute_script("$('select#spec-multiselect')[0].sumo.selectItem('Endokrynologia_i_diabetologia_dziecięca');")
    dane.logPerson(browser)
    time.sleep(2)
    browser.execute_script("document.getElementById('term_285').checked = true;"
                           "document.getElementById('term_224').checked = true;")
    browser.find_element_by_id("cartButton").click()
    time.sleep(5)
    dane.bramkaplatnosci(browser)
    return
