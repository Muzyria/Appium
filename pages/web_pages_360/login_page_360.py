
from pages.base_page import BasePage
from locators.web_locators_360 import LoginPageLocators


class LoginPage360(BasePage):
    def enter_user_to_site(self):
        """Вход пользователя на сайт"""
        self.element_is_visible(LoginPageLocators.INPUT_USERNAME).send_keys("QA")
        self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys("Qwerty01!")
        self.element_is_visible(LoginPageLocators.BUTTON_LOGIN).click()

