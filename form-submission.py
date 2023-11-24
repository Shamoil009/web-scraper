import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

os.environ["PATH"] += r"C:/SeleniumDrivers"

chromeWebDriverPath = "/chromedriver.exe"

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")


driver.implicitly_wait(5)


value1 = driver.find_element(By.ID, "value1")
value2 = driver.find_element(By.ID, "value2")

value1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
value2.send_keys(10)

btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()

sleep(30)
