import time
import pytest

from pages.base_page import BasePage
from locators.web_locators_360 import CourseMapPageLocators


class CourseMapPage(BasePage):
    def check_incoming_message(self, text_language, text_message_device):
        message_web = self.visibility_of_element_located(CourseMapPageLocators.TEXT_MESSAGE)
        text_message_web = message_web.text
        print(f"message on web - {text_message_web}")
        time.sleep(1)
        assert self.message_comparison(text_language, text_message_device, text_message_web), \
            f"the {text_language} message {text_message_device} does not match {text_message_web}"

    def message_comparison(self, language, text_message_device, text_message_web):
        if text_message_device != text_message_web:
            self.take_element_screenshot(CourseMapPageLocators.MODAL_WINDOW_MESSAGE, f"Expected {language} - {text_message_device}.png")
            self.visibility_of_element_located(CourseMapPageLocators.BUTTON_CONFIRMED_MESSAGE).click()
            return False
        self.visibility_of_element_located(CourseMapPageLocators.BUTTON_CONFIRMED_MESSAGE).click()
        return True

    def go_to_assets_page(self):
        button_assets = self.visibility_of_element_located(CourseMapPageLocators.BUTTON_ASSETS)
        button_assets.click()

    def press_cart_asset_details(self):
        button = self.visibility_of_element_located(CourseMapPageLocators.CART_ASSET_DETAILS)
        button.click()

    def check_gps_version(self, version_device):
        list_values = self.visibility_of_element_located(CourseMapPageLocators.LIST_VALUES_ASSET_DETAILS)
        values_gps = [item for item in list_values][2].text

        assert version_device == values_gps, f"Device GPS version {version_device} not math GPS version web {values_gps}"
        print(f"Gps version on web 360 is {values_gps}")
