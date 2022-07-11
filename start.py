import time
from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import accountInfoGenerator as account
import random

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

global_delay = 3

def delay(delay_time):
    log("Delay Baslangıc: " + str(delay_time))
    for i in range(delay_time, 0, -1):
        time.sleep(1)
        log("Delay Kalan: " + str(i))
    

if __name__ == '__main__':
    log('Bu program Can Tarafından Yapılmıştır.')
    log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
    log('Program başlatıldı')

def verif_mail(driver):
    #30 döngü
    tr_fs = 't'
    for i in range(30):
        if tr_fs == 't':
            try:
                driver.refresh()
                t = driver.title
                code = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/a").text
                log("Kod: " + code)
                code = code.replace(" is your Instagram code", "")
                code_lenght = len(code)
                tr_fs = 'f'
                return code
                break
            except:
                log("Verif mail kontrolü başarısız")
                delay(global_delay)
                continue
        else:
            delay(global_delay)
            continue


def create(proxy):
    print("Proxy: " + proxy)
    chrome_options=Options()
    chrome_options.add_argument('--proxy-server=%s'%proxy)
    driver = uc.Chrome(options=chrome_options)
    driver.delete_all_cookies()
    delay(1)
    driver.get('https://www.instagram.com/accounts/emailsignup/')
    driver.maximize_window()
    delay(1)
    driver.switch_to.new_window('tab')
    driver.get('https://www.moakt.com/tr')
    delay(4)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/span[3]/input").send_keys(account.username()+'cna')
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/input[2]").click()
    email_adress = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]').text
    #back to main tab
    driver.switch_to.window(driver.window_handles[0])
    try:
        cookie = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button[1]'))).click()
    except:
        pass
    name = account.username() + 'cna'
    password = account.generatePassword()
    driver.find_element(By.NAME, 'emailOrPhone').send_keys(email_adress)
    fullname_field = driver.find_element(By.NAME, 'fullName').send_keys(account.generatingName())
    log('Ad: ' + account.generatingName())
    username_field = driver.find_element(By.NAME, 'username').send_keys(name)
    log('K Adı: '+ name)
    password_field = driver.find_element(By.NAME, 'password').send_keys(password)
    log('Sifre: ' + password)
    log(name+":"+password)
    acco = open("acs.txt", "w", encoding='utf-8')
    datas = name + ":" + password
    acco.write(datas + "\n")
    acco.close()
    delay(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
    delay(5)
    driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

    driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

    driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
    delay(3)
    driver.switch_to.window(driver.window_handles[1])
    codeney = verif_mail(driver)
    log("Onay Kodu: " + codeney)
    delay(2)
    driver.switch_to.window(driver.window_handles[0])
    delay(2)
    driver.find_element(By.NAME, 'email_confirmation_code').send_keys(codeney, Keys.ENTER)
    log('Hesap Açıldı!')
    delay(10)
    driver.quit()

if __name__ == '__main__':
    kac_hesap = int(input("Kaç hesap oluşturmak istiyorsunuz? "))
    for i in range(kac_hesap):
        if __name__ == '__main__':
            #proxy.txt
            proxy = open("proxy.txt", "r", encoding='utf-8')
            proxy_list = proxy.readlines()
            proxy_random = random.choice(proxy_list)
            proxy_random = proxy_random.replace("\n", "")
            try:
                create(proxy_random)
            except:
                log("Hesap oluşturulamadı! Tekrar deneniyor...")
                delay(global_delay)
                #driver ı kapatıyoruz
                continue