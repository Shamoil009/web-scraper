import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        try:  # to cancel sign in popup
            no_button = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]'
            )
            no_button.click()
        except:
            print('No element with "Dismiss sign in information".')

        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        try:
            no_button = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'
            )
            no_button.click()
        except:
            print('No element with "Dismiss sign-in info."')

        selected_currency_element = self.find_elements(
            By.CSS_SELECTOR, 'button > div > div > span > div[class=" ea1163d21f"]'
        )

        for index, element in enumerate(selected_currency_element):
            # For example, you can print the text of each element
            if element.text == currency:
                print(selected_currency_element[index].text)
                selected_currency_element[index].click()
                break

                # print(element.text)

        # print(selected_currency_element[0].text)
        # selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        try:  # to cancel sign in popup
            no_button = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]'
            )
            no_button.click()
        except:
            print('No element with "Dismiss sign in information".')
            
        search_field = self.find_element(By.NAME, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
        sleep(5)
        first_result=self.find_element(By.CSS_SELECTOR,'div[data-testid="autocomplete-result"]')
        print(first_result.text)
        first_result.click()
