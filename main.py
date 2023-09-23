from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from notifypy import Notify

load_dotenv()

def div_check(driver:webdriver.Chrome):
        icon = "logo.png"
        direction = os.path.abspath(os.path.dirname(__file__))

        driver.get("https://prenotami.esteri.it/Services/Booking/340")
        time.sleep(5)

        div = driver.find_element(By.XPATH, "//div[@class='jconfirm jconfirm-light jconfirm-open']")

        if div.is_displayed():
              time.sleep(7200)
              div_check(driver)
        else:
            notification = Notify()
            notification.title = "TURNOS DISPONIBLES"
            notification.message = "HAY TURNOS DISPONIBLES"
            notification.icon = os.path.join(direction, icon)
            notification.send()

def main():
    driver = webdriver.Chrome()

    driver.get("https://prenotami.esteri.it/")

    mail = driver.find_element(By.XPATH, "//input[@name='Email']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    send = driver.find_element(By.XPATH, "//button[@class='button primary g-recaptcha']")

    mail.send_keys(os.getenv("IT_MAIL"))
    password.send_keys(os.getenv("IT_PASSWORD"))
    send.click()

    div_check(driver)

main()