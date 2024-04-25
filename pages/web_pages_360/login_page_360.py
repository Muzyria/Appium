
from pages.base_page import BasePage
from locators.web_locators_360 import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage360(BasePage):
    def enter_user_to_site(self):
        """Вход пользователя на сайт"""
        self.visibility_of_element_located(LoginPageLocators.INPUT_USERNAME).send_keys("QA")
        self.visibility_of_element_located(LoginPageLocators.INPUT_PASSWORD).send_keys("Qwerty01!")
        # self.wait.until(EC.)
        self.visibility_of_element_located(LoginPageLocators.BUTTON_LOGIN).click()


