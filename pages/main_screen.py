

from base_page import AppiumBasePage
from locators.android_locators import MainScreenLocators


class MainScreen(AppiumBasePage):
    def press_button_menu(self):
        button_menu = self.driver.find_elelement(*MainScreenLocators.BUTTON_MENU)
        button_menu.click()
