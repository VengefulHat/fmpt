# import bibliotek:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


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
    browser.get(dane.literkaprzedszkole_url)
    browser.maximize_window()
    time.sleep(2)
    dane.AdTerminator(browser)
    browser.find_element_by_xpath("//a[contains(text(),'Zaloguj')]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//a[contains(text(),'Zarejestruj się')]").click()
    time.sleep(2)
    while war == 0:
        if browser.current_url == 'https://www.literkaprzedszkole.pl/rejestracja':
            war += 1
        else:
            help += 1
            # tojest potrzebne jakby ta pętla mała trwać w nieskończonośći a tak
            # to się wywali jak należy
            if help > 100000:
                browser.save_screenshot(browser.current_url + ' ' + time.ctime())
                LogFile.error(browser.title, browser.current_url)
            continue
    war = 0
    help = 0
    browser.find_element_by_id("register-email").send_keys(poczta.name_mail())
    browser.find_element_by_name("phoneNumber").send_keys(dane.Phone)
    browser.find_element_by_name("firstName").send_keys(dane.Fname)
    browser.find_element_by_name("lastName").send_keys(dane.Lname)
    browser.execute_script("document.getElementById('agree1').checked = true;")
    time.sleep(1)
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)
    #LogFile.logowanie()
    print("Teraz wchodzimy w link do reejstracji z mailia:")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    browser.get(poczta.rejestracja())
    dane.AdTerminator(browser)
    browser.find_element_by_name("password[new]").send_keys(dane.haslo)
    browser.find_element_by_name("password[new-repeat]").send_keys(dane.haslo)
    time.sleep(2)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    # while war ==0:
    #     if browser.current_url == 'https://www.charakteryplus.pl/logowanie':
    #         war += 1
    #     if help == 10000:
    #         LogFile.error(browser.title, browser.current_url)
    #         break
    #     help =+ 1
    print("Rejestracja przebiegła poprawnie")
    time.sleep(3)
    return


def zamowienie():
    print("przechodzimy do zamówienia, na literce wybierzemy pakiet z firmą na rok")
    browser.find_element_by_class_name("cc-compliance").click()
    browser.find_element_by_xpath("//a[contains(text(),'Subskrybuj')]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//a[contains(@href, '/koszyk/zamow/2')]").click()# na rok
    time.sleep(2)
    # powinno być już zazaczone ale jeszcze raz jakby randomowo się to zazcnaczało
    #browser.find_element_by_xpath("(//a[contains(@href, '/logowanie')])[2]").click()# baton do logowania

    try:
        browser.find_element_by_xpath("//div[@id='nav-tab']/button[2]/span").click()  # na firmie
    except Exception as e:
        print(e)

    dane.logPerson(browser)
    time.sleep(1)
    browser.execute_script("document.getElementById('term_244').checked = true;"
                           "document.getElementById('term_224').checked = true;")
    browser.find_element_by_id("cartButton").click()
    time.sleep(5)
    return

# def zjemcie():
#     dra = webdriver.Firefox()
#     dra.get('https://panoramafirm.pl/wielkopolskie,,pozna%C5%84,je%C5%BCyce,polska,13/forum_media_polska_sp._z_o.o.-abiefy_bjm.html')
#     # time.sleep(2)
#     # dra.find_element_by_class_name('rodo-disable btn btn-primary').click()
#     # time.sleep(1)
#     # dra.find_element_by_id('cookie-disable').click()
#     # time.sleep(1)
#     # dra.find_element_by_class_name('btn btn-primary text-nowrap').click()
