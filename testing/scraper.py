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
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


chromeWebDriverPath = "/chromedriver.exe"

driver = webdriver.Chrome()
# driver.get("https://techwithtim.net")
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")


driver.implicitly_wait(5)
submit_button = driver.find_element(By.ID, "downloadButton")
submit_button.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"),  # element filtration
        "Complete!"
        # expected text
    )
)
print(submit_button.text)

# sleep(30)
