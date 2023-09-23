from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from notifypy import Notify

load_dotenv()

def div_check(driver:webdriver.Chrome):
        icon = "logo.ico"
        direction = os.path.abspath(os.path.dirname(__file__))

        driver.get("https://prenotami.esteri.it/Services/Booking/340")
        time.sleep(5)

        check = driver.current_url
        page = "https://prenotami.esteri.it/Services"

        if check != page:
              time.sleep(3600)
              div_check(driver)
        else:
            notification = Notify()
            notification.title = "TURNOS DISPONIBLES"
            notification.message = "HAY TURNOS DISPONIBLES"
            notification.icon = os.path.join(direction, icon)
            notification.send()
            time.sleep(5000)

def login(driver:webdriver.Chrome):
    driver.get("https://prenotami.esteri.it/")

    mail = driver.find_element(By.XPATH, "//input[@name='Email']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    send = driver.find_element(By.XPATH, "//button[@class='button primary g-recaptcha']")

    mail.send_keys(os.getenv("IT_MAIL"))
    password.send_keys(os.getenv("IT_PASSWORD"))
    send.click()

def main():
    driver = webdriver.Chrome()

    login(driver)
    
    check = driver.current_url
    page = "https://prenotami.esteri.it/Home/Login"

    if check != page:
        div_check(driver)
    else:
        time.sleep(5)
        driver.close()
        main()

main()