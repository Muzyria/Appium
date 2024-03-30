import time
import pytest

from pages.base_page import BasePage
from locators.web_locators import CourseMapPageLocators


class CourseMapPage(BasePage):
    def check_incoming_message(self, text_language, text_message_device):
        message_web = self.element_is_visible(CourseMapPageLocators.TEXT_MESSAGE)
        text_message_web = message_web.text
        print(f"message on web - {text_message_web}")
        time.sleep(1)
        assert self.message_comparison(text_language, text_message_device, text_message_web), \
            f"the {text_language} message {text_message_device} does not match {text_message_web}"

    def message_comparison(self, language, text_message_device, text_message_web):
        if text_message_device != text_message_web:
            self.take_element_screenshot(CourseMapPageLocators.MODAL_WINDOW_MESSAGE, f"Expected {language} - {text_message_device}.png")
            self.element_is_visible(CourseMapPageLocators.BUTTON_CONFIRMED_MESSAGE).click()
            return False
        self.element_is_visible(CourseMapPageLocators.BUTTON_CONFIRMED_MESSAGE).click()
        return True
