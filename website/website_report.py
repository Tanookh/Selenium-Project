# This file is going to include method that will parse the specific data that
# we need from each one of the deal boxes.

from selenium.webdriver.remote.webelement import WebElement


class WebsiteReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        # Pulling all the hotels in the page
        return self.boxes_section_element.find_elements_by_css_selector(
            'div[data-testid="property-card"]'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element_by_css_selector(
                'div[class="fde444d7ef _c445487e2"]'
            ).get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element_by_css_selector(
                'span[class="fde444d7ef _e885fdc12"]'
            ).get_attribute('innerHTML').strip()
            try:
                hotel_score = deal_box.find_element_by_css_selector(
                    'div[class="_9c5f726ff bd528f9ea6"]'
                ).get_attribute('innerHTML').strip()
            except:
                hotel_score = 'No Score'
            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection
