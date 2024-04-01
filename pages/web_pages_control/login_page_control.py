
from pages.base_page import BasePage
from locators.web_locators_control import LoginPageLocators


class LoginPageControl(BasePage):
    def enter_user_to_site(self):
        """Вход пользователя на сайт"""
        self.element_is_visible(LoginPageLocators.INPUT_USERNAME).send_keys("superadmin")
        self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys("superadmin")
        self.element_is_visible(LoginPageLocators.BUTTON_LOGIN).click()
