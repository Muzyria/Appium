
from locators.app_elements_page_locators import MainScreen
from pages.base_page import AppiumBasePage
# from appium.webdriver.common.mobileby import AppiumBy


class Page(AppiumBasePage):
    locators = MainScreen()

    def first(self):
        self.element_is_visible(self.locators.BUTTON_MENU).click()
        print("CLICk BUTTON MENU")

    def click_flag(self):
        self.touch_action(self.locators.BUTTON_FLAG)







