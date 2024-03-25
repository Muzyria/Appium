
from pages.base_page import BasePage


from selenium.webdriver import Keys


class SyncWiseSteps(BasePage):
    locators = SyncWise()

    def login_page_enter_syncwise(self):
        self.element_is_visible(self.locators.USER_NAME_SYNC).send_keys('QA')
        print("Input LOGIN")
        self.element_is_visible(self.locators.PASSWORD_SYNC).send_keys('Qwerty01!')
        print("Input PASSWORD")
        self.element_is_visible(self.locators.BUTTON_LOGIN_SYNC).click()
        print("Click BUTTON LOG IN")


