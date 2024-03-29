
from pages.base_page import AppiumBasePage
from locators.android_locators import MainScreenLocators


class MainScreen(AppiumBasePage):
    def press_button_menu(self):
        button_menu = self.element_is_visible(MainScreenLocators.BUTTON_MENU)
        button_menu.click()

    def press_button_select_language(self):
        button_language = self.element_is_visible(MainScreenLocators.BUTTON_LANGUAGE)
        button_language.click()
