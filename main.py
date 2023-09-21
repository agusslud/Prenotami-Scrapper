from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import pywhatkit

load_dotenv()

def div_check(driver:webdriver.Chrome):
        driver.get("https://prenotami.esteri.it/Services/Booking/340")
        time.sleep(5)

        div = driver.find_element(By.XPATH, "//div[@class='jconfirm jconfirm-light jconfirm-open']")

        if div.is_displayed():
              time.sleep(7200)
              div_check(driver)
        else:
              msg = "AMIGOOOOOO HAY TURNOS"
              num = os.getenv("IT_NUMBER")
              pywhatkit.sendwhatmsg_instantly(num, msg, tab_close=True)

def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://prenotami.esteri.it/")

    mail = driver.find_element(By.XPATH, "//input[@name='Email']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    send = driver.find_element(By.XPATH, "//button[@class='button primary g-recaptcha']")

    mail.send_keys(os.getenv("IT_MAIL"))
    password.send_keys(os.getenv("IT_PASSWORD"))
    send.click()

    div_check(driver)

main()