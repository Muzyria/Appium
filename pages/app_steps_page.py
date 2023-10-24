
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

    def swipe_my_down(self):
        self.swipe_screen_down()
        # self.swipe_screen_down()
        # self.swipe_screen_down()

    def swipe_my_up(self):
        self.swipe_screen_up()
        self.swipe_screen_up()
        self.swipe_screen_up()

    """Android menu and options"""
    def android_menu(self):
        self.long_press_key(26)
        self.element_is_visible(self.locators.ANDROID_WIDGET_PASSWORD).send_keys("102938")
        self.element_is_visible(self.locators.ANDROID_WIDGET_BUTTON_OK).click()

    def go_to_standby(self):
        self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_STANDBY).click()

    def go_to_power_off(self):
        self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_POWER_OFF).click()

    def go_to_restart(self):
        self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_RESTART).click()

    def go_to_ship_mode(self):
        self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_SHIP_MODE).click()
    """ - """


    def play_menu_and_password(self):
        """Click button MENU and enter password"""
        self.element_is_visible(self.locators.BUTTON_MENU).click()
        print("CLICk BUTTON MENU")
        self.









