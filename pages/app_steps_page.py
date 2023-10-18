
from locators.app_elements_page_locators import MainScreen
from pages.base_page import AppiumBasePage


class Page(AppiumBasePage):
    locators = MainScreen()

    def first(self):
        self.element_is_visible(self.locators.BUTTON_MENU).click()








