import time

from pages.base_page import BasePage
from locators.web_locators import LoginPageLocators


class LoginPage(BasePage):
    def click_button_add_to_bucket(self):
        # button_add = self.driver.find_element(*LoginPageLocators.BUTTON_ADD_TO_BASKET)
        button_add = self.element_is_visible(LoginPageLocators.BUTTON_ADD_TO_BASKET)
        # time.sleep(5)
        button_add.click()
        time.sleep(5)