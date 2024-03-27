import time

from pages.base_page import BasePage
from locators.web_locators import CourseMapPageLocators


class CourseMapPage(BasePage):
    def check_incoming_message(self):
        text_message = self.element_is_visible(CourseMapPageLocators.TEXT_MESSAGE).text
        print(f"-------{text_message}--------")
        time.sleep(1)
        self.element_is_visible(CourseMapPageLocators.BUTTON_CONFIRMED_MESSAGE).click()
