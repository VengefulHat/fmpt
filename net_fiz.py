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

def logowanie():
    global browser
    war = 0
    help = 0
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(dane.net_fiz_url)
    browser.maximize_window()
    time.sleep(3)
    AdTerminator()
    browser.find_element_by_xpath("//a[contains(text(),'Zaloguj')]").click()
    time.sleep(3)
    browser.find_element_by_xpath("//a[contains(text(),'Zarejestruj się')]").click()
    time.sleep(2)
    while war == 0:
        if browser.current_url == 'https://www.net-fiz.pl/rejestracja':
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
    print("koniec")




def AdTerminator():
    t0 = time.time()
    i = 0
    while i == 0:
        time.sleep(7)
        elements2 = browser.find_elements_by_id("smPopupCloseButton")
        if len(elements2) > 0:
            if len(elements2) > 0:
                browser.find_element_by_id("smPopupCloseButton").click()
                i += 1
                print(elements2)
            else:
                continue
            t1 = time.time()
            td = t0 - t1
            if td > 6:
                i += 1
            else:
                continue
        else:
            break
    return
