# tutaj trzymamy zmienne
# czasem zmienne stałe
from selenium.webdriver.common.by import By
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
    ify = browser.find_elements(By.TAG_NAME, "iframe")
    browser.switch_to.frame(ify[0])
    browser.find_element(By.XPATH, "//a[contains(.,'Załóż konto')]").click()
    print("jestemsmy juz tutaj")
    #browser.find_element(By.ID, "externalLink").click()
    ify = browser.find_elements(By.TAG_NAME, "iframe")
    print(len(ify))
    print("wyżej wydrukowałem ile jest iframow")
    browser.switch_to.frame(ify[0])
    print('Wybieramy takie jednego iframa obama')
    browser.find_element(By.ID, "app_user_registration_email").send_Keys(poczta.name_mail())
    browser.find_element(By.ID, "app_user_registration_firstName").send_keys(Fname)
    browser.find_element(By.ID, "app_user_registration_lastName").send_keys(Lname)
    browser.find_element(By.ID, "app_user_registration_phoneNumber").send_keys(Phone)
    time.sleep(1)
    browser.find_element(By.ID, "registerSubmit").click()
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
    browser.find_element_by_id("address").send_keys(adress)
    browser.find_element_by_id("house-number").send_keys(numberhouse)
    browser.find_element_by_id("city").send_keys(miasto)
    browser.find_element_by_id("postal-code").send_keys(kodpocztowy)
    browser.find_element_by_id("emailToSendInvoice").send_keys(poczta.email)
    try:
        browser.find_element_by_id("address").send_keys(adress)
    except Exception as e:
        print(e)
    time.sleep(1)
    browser.find_element_by_xpath("(//button[@type='submit'])[2]").click()
    return

def logCompany(browser):
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
    try:
        browser.find_element_by_name("firstName").send_keys(Fname).click()  # na test
    except Exception as e:
        print(e)
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
    t0 = time.time()
    i = 0
    while i == 0:
        forpopup = browser.find_elements(By.TAG_NAME, "iframe")
        print(len(forpopup))
        browser.switch_to.frame(forpopup[4])

        time.sleep(7)
        browser.find_element_by_xpath("//div[@class='bhr-ip__b']/div[@class='bhr-ip__c']/div[1]").click()
        elements2 = browser.find_elements_by_class_name("bhr-ip__c__close ip-close-event bhr-ip__c__close--3")
        print(len(elements2))
        if len(elements2) > 0:
            if len(elements2) > 0:
                print("Niby klika")
                browser.find_element_by_class_name("bhr-ip__c__close ip-close-event bhr-ip__c__close--3").click()
                i += 1
                print(elements2)
                browser.switch_to.default_content()
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


#bhr-ip__c__close ip-close-event bhr-ip__c__close--3
# url's
literkaprzedszkole_url = 'https://www.literkaprzedszkole.pl/'
pediatriaplus_url = 'https://www.pediatriaplus.pl/'
net_fiz_url = 'https://www.net-fiz.pl/'
animalexpertplus_url = 'https://www.animalexpertplus.pl/'
doradcaksiegowego_url = 'https://www.doradcaksiegowego.pl/'
charakteryplus_url = 'https://www.charakteryplus.pl/'
forumginekologii_url = 'https://www.forumginekologii.pl/'