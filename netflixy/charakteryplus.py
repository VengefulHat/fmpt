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
    browser.get(dane.charakteryplus_url)
    browser.maximize_window()
    time.sleep(2)
    dane.AdTerminator(browser)
    browser.find_element_by_xpath("//a[contains(text(),'Zaloguj')]").click()
    time.sleep(3)
    browser.find_element_by_xpath("//a[contains(text(),'Zarejestruj się')]").click()
    time.sleep(2)
    while war == 0:
        if browser.current_url == 'https://www.charakteryplus.pl/rejestracja':
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
    # while war == 0:
    #     if browser.current_url == 'https://www.charakteryplus.pl/logowanie':
    #         war += 1
    #     if help == 10000:
    #         LogFile.error(browser.title, browser.current_url)
    #         break
    #     help = + 1
    print("Rejestracja przebiegła poprawnie")
    time.sleep(3)
    return


def zamowienie():
    print("przechodzimy do zamówienia, na charakteryplus wybierzemy pakiet z jednostkabudżetowa na unitstuff")
    browser.find_element_by_class_name("cc-compliance").click()
    time.sleep(5)
    browser.find_element_by_xpath("//a[contains(@href, '/oferta')]").click()
    try:
        browser.find_element_by_xpath("//a[contains(@href, 'https://www.charakteryplus.pl/koszyk/zamow/54')]").click()  # testowe
    except Exception as e:
        print(e)

    time.sleep(2)
    # powinno być już zazaczone ale jeszcze raz jakby randomowo się to zazcnaczało
    # browser.find_element_by_xpath("(//a[contains(@href, '/logowanie')])[2]").click()# baton do logowania
    try:
        browser.find_element_by_class_name("#nav-tab > .nav-item:nth-child(4)").click()  # na jednostkę budżetową
    except Exception as e:
        print(e)
    try:
        browser.find_element_by_xpath("//div[@id='nav-tab']/button[3]/span").click()  # na jednostkę budżetową
    except Exception as e:
        print(e)
    time.sleep(2)
    dane.logUnitStuff(browser)
    time.sleep(2)
    browser.execute_script("document.getElementById('term_251').checked = true;"
                           "document.getElementById('term_224').checked = true;")
    browser.find_element_by_id("cartButton").click()
    time.sleep(5)
    dane.bramkaplatnosci(browser)
    return
