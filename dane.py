# tutaj trzymamy zmienne
# czasem zmienne stałe
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#import własnych plików
import poczta


# const data
stanowisko = 'Siedzące'
Fname = 'Test'
Lname = 'Testowy'
Phone = 123456789
npwz = 3313581
specjalizacja = ''
haslo = 'Bartek1.'
adress = 'Polska'
kodpocztowy = '60-595'
numberhouse = 13
miasto = 'Poznań'
company_name = 'Cyrkon-95'
nip = 4721875044
odbiorca_Fname = 'Zbigniew'
odbiorca_Lname = 'Pleisner'
odbiorca_company ='MAcriciosa'
odbiorca_ulica = 'Wielkopolska'
odbiorca_numer_domu = 14
odbiorca_miasto = 'Poznań'
odbiorca_kod_pocztowy = '60-696'


def logowanie_cms(browser):
    """
    to tak naprawde rejestracja, nie chce zmianiać dla tego nazwy i przypisów itp
    blok od zamówień będzie logował się z automatu i składał zamówienie (w jedym def-ie wszystko)
    :param browser:
    :return:
    """
    time.sleep(1)
    try:
        browser.find_element(By.CLASS_NAME, "cc-compliance").click()
    except Exception:
        pass
    time.sleep(2)
    ifa = browser.find_elements(By.TAG_NAME, "iframe")
    browser.switch_to.frame(ifa[0])
    browser.find_element(By.XPATH, "//a[contains(.,'Załóż konto')]").click()
    browser.switch_to.default_content()
    time.sleep(1)
    print("Sprawdzamy iframe od panelu logowania")
    ify = browser.find_elements(By.TAG_NAME, "iframe")
    print(len(ify), "tyle jest iframe")
    browser.switch_to.frame(ify[0])
    more = browser.find_elements(By.ID, "app_user_registration_email")
    print(len(more), " dla iframe 1")
    browser.switch_to.default_content()
    browser.switch_to.frame(ify[1])
    more = browser.find_elements(By.ID, "app_user_registration_email")
    print(len(more), " dla iframe 2")
    browser.find_element(By.ID, "app_user_registration_email").send_keys(poczta.name_mail())
    browser.find_element(By.ID, "app_user_registration_firstName").send_keys(Fname)
    browser.find_element(By.ID, "app_user_registration_lastName").send_keys(Lname)
    browser.find_element(By.ID, "app_user_registration_phoneNumber").send_keys(Phone)
    time.sleep(1)
    try:
        browser.find_element(By.ID, "registerSubmit").click()
        print("aaaa")
    except Exception:
        print("klikam raz")
        pass
    try:
        browser.find_element(By.ID, "registerSubmit").click()
        print("aaaaaa")
    except Exception:
        print("klikam dwa")
        pass
    browser.switch_to.default_content()
    return

def bramkaplatnosci(browser):
    aqa = browser.find_elements(By.TAG_NAME, "iframe")
    browser.switch_to.frame(aqa[0])
    browser.find_element(By.NAME, "cardNumber").send_keys(4916123217709315)
    browser.switch_to.default_content()
    browser.switch_to.frame(aqa[1])
    browser.find_element(By.NAME, "expDate").send_keys(1125)
    browser.switch_to.default_content()
    browser.switch_to.frame(aqa[2])
    browser.find_element(By.NAME, "cvv").send_keys(342)
    browser.switch_to.default_content()
    browser.execute_script("document.getElementById('payment-agreement').checked = true;")
    browser.find_element(By.ID, "tokenizeButton").click()
    time.sleep(10)
    return

def logPerson(browser):
    time.sleep(4)


    #browser.execute_script("$('#address').val('Polska');")
    browser.execute_script("document.querySelectorAll('*[name=\"address\"]')[0].value = 'Polska';")
    #browser.find_element_by_id("address").send_keys(adress)
    #browser.execute_script("$('#house-number').val('13');")
    browser.execute_script('document.getElementById("house-number").value = "13";')
    #browser.find_element_by_id("house-number").send_keys(numberhouse)
    #browser.execute_script("$('#address').val('Polska');")
    browser.execute_script('document.getElementById("city").value = "Poznań";')
    #browser.find_element_by_id("city").send_keys(miasto)
    #browser.execute_script("$('#address').val('Polska');")
    browser.execute_script('document.getElementById("postal-code").value = "60-595";')
    #browser.find_element_by_id("postal-code").send_keys(kodpocztowy)
    browser.find_element_by_id("emailToSendInvoice").send_keys(poczta.email)
    # try:
    #     browser.find_element_by_id("address").send_keys(adress)
    # except Exception as e:
    #     print(e)
    time.sleep(1)
    browser.find_element_by_xpath("(//button[@type='submit'])[2]").click()
    return

def logCompany(browser):
    time.sleep(4)
    browser.find_element_by_id("company-name").send_keys(company_name)
    browser.find_element_by_id("company-nip").send_keys(nip)
    browser.find_element_by_id("address").send_keys(adress)
    browser.find_element_by_id("house-number").send_keys(numberhouse)
    browser.find_element_by_id("city").send_keys(miasto)
    browser.find_element_by_id("postal-code").send_keys(kodpocztowy)
    browser.find_element_by_id("emailToSendInvoice").send_keys(poczta.email)
    time.sleep(1)
    browser.find_element_by_xpath("(//button[@type='submit'])[2]").click()
    return

def logUnitStuff(browser):
    time.sleep(4)
    try:
        browser.find_element_by_name("firstName").send_keys(Fname).click()  # na test
    except Exception as e:
        print(e)
    browser.implicitly_wait(time_to_wait=5)
    try:
        browser.find_element_by_name("lastName").send_keys(Lname).click()  # na test
    except Exception as e:
        print(e)

    browser.find_element_by_id("phone-number").send_keys(Phone)

    browser.find_element_by_id("position").send_keys(stanowisko)

    browser.find_element_by_id("company-name").send_keys(company_name)

    browser.find_element_by_id("company-nip").send_keys(nip)

    browser.find_element_by_id("address").send_keys(adress)

    browser.find_element_by_id("house-number").send_keys(numberhouse)

    browser.find_element_by_id("city").send_keys(miasto)

    browser.find_element_by_id("postal-code").send_keys(kodpocztowy)

    browser.find_element_by_id("recipient-first-name").send_keys(odbiorca_Fname)

    browser.find_element_by_id("recipient-last-name").send_keys(odbiorca_Lname)

    browser.find_element_by_id("recipient-company").send_keys(odbiorca_company)

    browser.find_element_by_id("recipient-address").send_keys(odbiorca_ulica)

    browser.find_element_by_id("recipient-house-number").send_keys(odbiorca_numer_domu)

    browser.find_element_by_id("recipient-city").send_keys(odbiorca_miasto)

    browser.find_element_by_id("recipient-postal-code").send_keys(odbiorca_kod_pocztowy)

    browser.find_element_by_id("emailToSendInvoice").send_keys(poczta.email)
    time.sleep(1)
    browser.find_element_by_xpath("(//button[@type='submit'])[2]").click()
    return

def AdTerminator(browser):
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

def cmspopupshutup(browser):
    time.sleep(5)
    forpopup = browser.find_elements(By.TAG_NAME, "iframe")
    browser.switch_to.frame(forpopup[1])
    time.sleep(2)
    try:

        browser.find_element_by_class_name("fa-2x").click()
    except Exception as d:
        print(d)
    try:

        browser.find_element_by_class_name("bhr-ip__c__close ip-close-event bhr-ip__c__close--3").click()
    except Exception as d:
        print(d)
    browser.refresh()
    time.sleep(3)
    print("Reklama zamknięta")
    browser.switch_to.default_content()
    return

def logCompany_CMS(browser):
    browser.find_element_by_name("order[orderingPersonDetails][lastName]").send_keys(Lname)
    browser.find_element_by_name("order[orderingPersonDetails][position]").send_keys(stanowisko)
    browser.find_element_by_name("order[billing][address]").send_keys(adress)
    browser.find_element_by_name("order[billing][houseNumber]").send_keys(numberhouse)
    browser.find_element_by_name("order[billing][postalCode]").send_keys(kodpocztowy)
    browser.find_element_by_name("order[billing][city]").send_keys(miasto)
    browser.find_element_by_name("order[billing][companyName]").send_keys(company_name)
    browser.find_element_by_name("order[billing][nip]").send_keys(nip)
    return

def logPerson_CMS(browser):
    browser.find_element_by_name("order[orderingPersonDetails][lastName]").send_keys(Lname)
    #browser.find_element_by_name("order[orderingPersonDetails][position]").send_keys(stanowisko)
    browser.find_element_by_name("order[billing][address]").send_keys(adress)
    browser.find_element_by_name("order[billing][houseNumber]").send_keys(numberhouse)
    browser.find_element_by_name("order[billing][postalCode]").send_keys(kodpocztowy)
    browser.find_element_by_name("order[billing][city]").send_keys(miasto)
    return


#bhr-ip__c__close ip-close-event bhr-ip__c__close--3
# url's
literkaprzedszkole_url = 'https://www.literkaprzedszkole.pl/'
pediatriaplus_url = 'https://www.pediatriaplus.pl/'
net_fiz_url = 'https://www.net-fiz.pl/'
animalexpertplus_url = 'https://www.animalexpertplus.pl/'
doradcaksiegowego_url = 'https://www.doradcaksiegowego.pl/'
charakteryplus_url = 'https://www.charakteryplus.pl/'
forumginekologii_url = 'https://www.forumginekologii.pl/'
praktycznafizjoterapia_url = 'https://www.praktycznafizjoterapia.pl/'
charaktery_url = 'https://charaktery.eu/'
psychologiawpraktyce_url = 'https://psychologiawpraktyce.pl/'
forumlogopedy_url = 'https://forumlogopedy.pl/'