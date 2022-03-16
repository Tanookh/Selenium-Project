# This file will include a class with instance methods
# that will be responsible with interacting with our website
# after we have some results to apply filtrations.

from selenium.webdriver.remote.webdriver import WebDriver


class WebsiteFiltration:
    def __int__(self, driver: WebDriver = None):
        self.driver = driver

    def init_driver(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_value=None):
        star_class_element = self.driver.find_element_by_css_selector(
            f'div[data-filters-item="class:class={star_value}"]'
        )
        star_class_element.click()
