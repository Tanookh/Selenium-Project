import website.constants as const
import os
from selenium import webdriver
from website.website_filtration import WebsiteFiltration


# A class and functions for the webpage
class Website(webdriver.Chrome):

    # Constructor for Website that gives the driver location and runs it
    def __init__(self, driver_path=r"D:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Website, self).__init__()
        self.implicitly_wait(15)  # Wait for the element to appear or wait 15 seconds
        self.maximize_window()  # Start with a full screen

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
    def change_country(self, language=None):
        country_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your language"]'
        )
        country_element.click()
        selected_country_element = self.find_element_by_css_selector(
            f'a[data-lang="{language}"]'
        )
        selected_country_element.click()

    # Select the destination
    def select_destination(self, destination=None):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(destination)
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    # Select Check-in and Check-out
    def select_dates(self, check_in_date=None, check_out_date=None):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    # Select adults
    def select_adults(self, count=1):
        # To make sure adults stay in range
        if count < 1:
            count = 1
        if count > 30:
            count = 30
        adults_element = self.find_element_by_id('xp__guests__toggle')
        adults_element.click()
        sub_adults_element = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        adults_value_element = self.find_element_by_id('group_adults')
        adults_value = adults_value_element.get_attribute(
            'value'
        )  # Gives the adults count
        while adults_value != '1':
            sub_adults_element.click()
            adults_value = adults_value_element.get_attribute(
                'value'
            )  # Gives the adults count
        add_adults_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        while adults_value != count.__str__():
            add_adults_element.click()
            adults_value = adults_value_element.get_attribute(
                'value'
            )  # Gives the adults count

    # Click search function
    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtration(self, star_value):
        filtration = WebsiteFiltration()
        filtration.init_driver(driver=self)
        filtration.apply_star_rating(star_value)
