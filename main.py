from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import http.client, urllib

load_dotenv()

def div_check(driver:webdriver.Chrome):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        
        driver.get("https://prenotami.esteri.it/Services/Booking/340")
        time.sleep(5)

        div = driver.find_element(By.XPATH, "//div[@class='jconfirm jconfirm-light jconfirm-open']")

        if div.is_displayed():
              time.sleep(3600)
              div_check(driver)
        else:
            conn.request("POST", "/1/messages.json",
              urllib.parse.urlencode({
                "token": os.getenv("APP_TOKEN"),
                "user": os.getenv("USER_KEY"),
                "title": "TURNOS",
                "message": "Hay un turno disponible",
                "priority": "1"
              }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()

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
