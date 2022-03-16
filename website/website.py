import website.constants as const
import os
from selenium import webdriver

# A class and functions for the webpage
class Website(webdriver.Chrome):

    # Constructor for Website that gives the driver location and runs it
    def __init__(self, driver_path=r"D:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Website, self).__init__()
        self.implicitly_wait(15) # Wait for the element to appear or wait 15 seconds
        self.maximize_window() # Start with a full screen

    # Choose if to exit the webpage or not after running
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # For opening the web page
    def land_first_page(self):
        self.get(const.BASE_URL)

    # Change the currency
    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    # Change the country
    def change_country(self, country=None):
        country_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your language"]'
        )
        country_element.click()
        selected_country_element = self.find_element_by_css_selector(
            f'a[data-lang="{country}"]'
        )
        selected_country_element.click()