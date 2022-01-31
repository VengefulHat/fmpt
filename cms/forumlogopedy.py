# import bibliotek:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys


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
    browser.get(dane.forumlogopedy_url)
    browser.maximize_window()
    time.sleep(4)
    print("przechodzimy do def zamykania reklamy ")
    dane.cmspopupshutup(browser)
    time.sleep(1)
    #browser.find_element_by_xpath("//footer[@id='footer']/div[@role='dialog']//a[@role='button']").click()
    time.sleep(1)
    dane.logowanie_cms(browser)
    print("Teraz wchodzimy w link do reejstracji z mailia:")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    browser.get(poczta.rejestracjaCMS())
    time.sleep(3)
    akar = browser.find_elements(By.TAG_NAME, "iframe")
    browser.switch_to.frame(akar[1])
    print("gurwa teraz")
    #aaa = browser.find_elements(By.ID, "fos_user_resetting_plainPassword_first")
    browser.find_element(By.ID, "fos_user_resetting_plainPassword_first").send_keys(dane.haslo)
    browser.find_element(By.ID, "fos_user_resetting_plainPassword_second").send_keys(dane.haslo)
    time.sleep(1)
    try:
        browser.find_element(By.CLASS_NAME, "btn login-content-submit").click()
    except Exception as e:
        print(e)
    try:
        browser.find_element(By.CSS_SELECTOR, '.login-content-submit').click()
    except Exception as e:
        print(e)

    try:
        browser.find_element_by_class_name("btn login-content-submit").click()
    except Exception as e:
        print(e)

    try:
        browser.find_element_by_class_name("btn login-content-submit").click()
    except Exception as e:
        print(e)

    try:
        browser.find_element_by_class_name("btn login-content-submit").click()
    except Exception as e:
        print(e)

    time.sleep(3)
    browser.switch_to.default_content()
    print("Rejestracja przebiegła poprawnie")
    time.sleep(3)
    browser.refresh()

    return


def zamowienie():
    print("Zaczynamy sekcje od zamówienia")
    time.sleep(3)
    ilehh = browser.find_elements(By.TAG_NAME, 'iframe')
    ######
    time.sleep(2)
    browser.switch_to.frame(ilehh[1])
    qw = browser.find_elements(By.NAME, "_username")
    print(len(qw))
    #####mam iframe od panelu logowania
    time.sleep(1)
    browser.find_element(By.NAME, "_username").send_keys(poczta.email)
    browser.find_element(By.NAME, "_password").send_keys(dane.haslo)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, ".btn.login-content-submit.login-submit").click()
    print("Logowanie zakończone")
    browser.switch_to.default_content()
    # tu się kończy logowanie !!!!
    sys.stdout.flush()
    time.sleep(3)
    time.sleep(1)
    sys.stdout.flush()
    time.sleep(1)
    print("Jebany program o chuj chodzi")
    time.sleep(1)
    print("Wrzucam kom co sekundę bo mi pomija ten czas 5 s")
    time.sleep(1)
    print("I sie strona załadowac nie zdąży")
    browser.find_element(By.CSS_SELECTOR, "input[name='terms[4]']").click()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[10]/div[@role='dialog']/div[@class='swal2-buttonswrapper']/button[1]").click()

    popo = browser.find_elements(By.CLASS_NAME, "swal2-confirm swal2-styled")
    print(len(popo))

    #browser.execute_script("document.querySelector('.input[name=\"terms[53]\"]').checked = true;")
    #document.querySelector(".example")
    """
    Koniec i ze zgodami 
    teraz czas na zamówienie w końcu 
    """


    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "picture").click()


    print("przechodzimy do zamówienia, na foumginekologii wybierzemy pakiet z firmą")
    browser.find_element_by_xpath("/html//div[@class='main-bar']/div/div//a[@href='/prenumerata']").click()
    time.sleep(2)

    try:
        browser.find_element_by_xpath("/html//div[@id='wybor-prenumeraty']//div[@class='prenumerata-2k21-box']/button[@type='button']").click()
    except Exception:
        print("raz")
    try:
        browser.find_element_by_xpath("/html//div[@id='wybor-prenumeraty']//div[@class='prenumerata-2k21-box']/button[@type='button']").click()
    except Exception:
        print("dwa")
    #browser.find_element_by_xpath("//a[contains(@href, '/koszyk/zamow/45')]").click()# na rok
    #browser.find_element_by_xpath("//a[contains(text(),'Wybieram')]")
    time.sleep(2)
    a = browser.find_elements(By.TAG_NAME, 'iframe')
    print(len(a))
    time.sleep(5)
    browser.refresh()

    time.sleep(1)
    browser.switch_to.frame(browser.find_elements(By.TAG_NAME, 'iframe')[1])
    browser.find_element(By.CSS_SELECTOR, 'button[name="save"]').click()
    time.sleep(7)

    tagi = browser.find_elements(By.TAG_NAME, 'iframe')
    a = 0
    print(len(tagi))
    print("teraz czekamy na wyniki z przszukiwania strony")
    time.sleep(5)

    z = browser.find_elements_by_id("clientType-clienttype-budgetunit")

    #x = browser.find_elements_by_id("app_user_registration_firstName")
    # m = browser.find_elements_by_id("order_orderingPersonDetails_lastName")
    n = browser.find_elements_by_name("order[orderingPersonDetails][lastName]")
    # b = browser.find_elements_by_id("order_billing_address")
    # v = browser.find_elements_by_id("app_user_registration_firstName")

    y = browser.find_elements_by_name("save")

    if len(z) > 0:
        print("Jestem w ", a, "iframie dla radiobutton")

    if len(n) > 0:
        print("Jestem w ", a, "iframie dla emialregistration")

    if len(y) > 0:
        print("Jestem w ", a, "iframie dla batona safe")
    # while a != len(tagi):
    #     browser.switch_to.frame(tagi[a])
    #
    #     z = browser.find_elements_by_id("clientType-clienttype-budgetunit")
    #     x = browser.find_elements_by_id("app_user_registration_firstName")
    #     y = browser.find_elements_by_name("save")
    #
    #     if len(z) > 0:
    #         print("Jestem w ", a, "iframie dla radiobutton")
    #
    #     if len(x) > 0:
    #         print("Jestem w ", a, "iframie dla emialregistration")
    #
    #     if len(y) > 0:
    #         print("Jestem w ", a, "iframie dla batona safe")
    #
    #     browser.switch_to.default_content()
    #     print("okrążenie numer: ", a)
    #     a += 1

    """
    Informacje dla potomnych
    dla radioboxów na CMS od / jednostka budżetowa / firma / osoba prywatna /
    najepiej po id: 
    jednostka budżetowa = <input id="clientType-clienttype-budgetunit"> 
    osoba prywatna = <input id="clientType-clienttype-privateperson">
    firma = <input id="clientType-clienttype-business">
    """
    browser.execute_script("document.getElementById('clientType-clienttype-business').checked = true;")
    time.sleep(2)
    ########################### TO DZIAŁA JAK NALEŻY
    browser.execute_script("document.getElementById('clientType-clienttype-privateperson').checked = true;")
    browser.execute_script("document.getElementById('clientType-clienttype-privateperson').checked = true;")
    browser.execute_script("document.getElementById('clientType-clienttype-privateperson').checked = true;")
    try:
        iframe_1 = browser.find_element(By.XPATH, "/html//iframe[@id='iframe-cart']")
        browser.switch_to.frame(iframe_1)
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, 'clientType btn order-address-client-type-button ').click()
        time.sleep(1)
        browser.switch_to.default_content()
    except Exception:
        pass
    time.sleep(4)
    # browser.execute_script("document.getElementById('clientType-clienttype-privateperson').checked = true;")
    ########################### TO DZIAŁA JAK NALEŻY

    #browser.find_element_by_id("clientType-clienttype-privateperson").click()
    dane.logCompany_CMS(browser)
    # browser.find_element_by_name("order[orderingPersonDetails][lastName]").send_keys(dane.Lname)
    # browser.find_element_by_name("order[orderingPersonDetails][position]").send_keys(dane.stanowisko)
    # browser.find_element_by_name("order[billing][address]").send_keys(dane.adress)
    # browser.find_element_by_name("order[billing][houseNumber]").send_keys(dane.numberhouse)
    # browser.find_element_by_name("order[billing][postalCode]").send_keys(dane.kodpocztowy)
    # browser.find_element_by_name("order[billing][city]").send_keys(dane.miasto)
    # browser.find_element_by_name("order[billing][companyName]").send_keys(dane.company_name)
    # browser.find_element_by_name("order[billing][nip]").send_keys(dane.nip)

    browser.find_element(By.XPATH, "//select[@id='order_orderingPersonDetails_position']/option[@value='16']").click()


    time.sleep(1)

    browser.find_element_by_name("save").click()

    time.sleep(1)

    browser.find_element_by_id("orderTermsCheckAll").click()
    time.sleep(1)
    browser.find_element_by_name("save").click()
    print("Koniec składania zamówienia CMS")
    return
