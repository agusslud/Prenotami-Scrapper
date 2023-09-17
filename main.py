from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import schedule

load_dotenv()

def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://prenotami.esteri.it/")

    mail = driver.find_element(By.XPATH, "//input[@name='Email']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    send = driver.find_element(By.XPATH, "//button[@class='button.primary']")

    mail.send_keys(os.getenv("IT_MAIL"))
    password.send_keys(os.getenv("IT_PASSWORD"))
    send.click()

    driver.get("https://prenotami.esteri.it/Services/Booking/340")
    container = driver.find_element(By.XPATH, "//div[@class='']")
    container.click()

    time.sleep(3600)

main()