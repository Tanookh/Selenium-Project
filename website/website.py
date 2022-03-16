import website.constants as const
import os
from selenium import webdriver

# A class and functions for the webpage
class Website:

    # Constructor for Website that gives the driver location and runs it
    def __init__(self):
        self.driver = webdriver.Chrome(const.chrome_driver_path)

    # For opening the web page
    def land_first_page(self):
        self.driver.get(const.BASE_URL)
