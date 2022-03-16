import website.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# A class and functions for the webpage


class Website(webdriver.Chrome):

    # Constructor for Website that gives the driver location and runs it
    def __init__(self, driver_path=r"D:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Website, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    # Choose if to exit the webpage or not after running
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # For opening the web page
    def land_first_page(self):
        self.get(const.BASE_URL)
