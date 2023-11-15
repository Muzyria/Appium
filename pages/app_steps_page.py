
from locators.app_elements_page_locators import MainScreen
from pages.base_page import AppiumBasePage


class AutomaticAPKOSUpdate(AppiumBasePage):
    locators = MainScreen()

    def from_main_page_to_settings(self):
        self.element_is_visible(self.locators.BUTTON_MENU).click()
        self.element_is_visible(self.locators.BUTTON_SETTINGS).click()
        self.element_is_visible(self.locators.BUTTON_1).click()
        self.element_is_visible(self.locators.BUTTON_2).click()
        self.element_is_visible(self.locators.BUTTON_3).click()
        self.element_is_visible(self.locators.BUTTON_9).click()
        self.element_is_visible(self.locators.BUTTON_9).click()
        self.element_is_visible(self.locators.BUTTON_9).click()
        self.element_is_visible(self.locators.BUTTON_SUBMIT).click()

    def case_one_steps(self):
        self.from_main_page_to_settings()

        self.element_is_visible(self.locators.BUTTON_ASSET_DETAILS_MENU_SETTINGS).click()
        
        self.swipe_screen_down()
        self.take_element_screenshot(self.locators.TEXT_VIEW_APPLICATION_VERSION_APK_VALUE_ASSET_DETAILS, 'apk_version')
        apk_version = self.element_is_visible(self.locators.TEXT_VIEW_APPLICATION_VERSION_APK_VALUE_ASSET_DETAILS).text

        self.element_is_visible(self.locators.BUTTON_CANCEL_ASSET_DETAILS).click()
        self.element_is_visible(self.locators.BUTTON_CANCEL_MENU_SETTINGS).click()
        self.element_is_visible(self.locators.BUTTON_PLAY_GOLF).click()
        return apk_version


    # def second(self):
    #     self.element_is_visible(self.locators.BUTTON_PLAY_GOLF).click()
    #     print("CLICk BUTTON PLAY GOLF")
    #
    # def third(self):
    #     self.element_is_visible(self.locators.BUTTON_ASSET_DETAILS_MENU_SETTINGS).click()
    #     print("CLICk BUTTON ASSET DETAILS")
    #
    # def fourth(self):
    #     return self.element_is_visible(self.locators.TEXT_VIEW_APPLICATION_VERSION_APK_VALUE_ASSET_DETAILS).text
    #
    # def click_flag(self):
    #     self.touch_action(self.locators.BUTTON_FLAG)
    #
    # def swipe_my_down(self):
    #     self.swipe_screen_down()
    #     # self.swipe_screen_down()
    #     # self.swipe_screen_down()
    #
    # def swipe_my_up(self):
    #     self.swipe_screen_up()
    #     # self.swipe_screen_up()
    #     # self.swipe_screen_up()
    #
    # """Android menu and options"""
    # def android_menu(self):
    #     self.long_press_key(26)
    #     self.element_is_visible(self.locators.ANDROID_WIDGET_PASSWORD).send_keys("102938")
    #     self.element_is_visible(self.locators.ANDROID_WIDGET_BUTTON_OK).click()
    #
    # def go_to_standby(self):
    #     self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_STANDBY).click()
    #
    # def go_to_power_off(self):
    #     self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_POWER_OFF).click()
    #
    # def go_to_restart(self):
    #     self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_RESTART).click()
    #
    # def go_to_ship_mode(self):
    #     self.element_is_visible(self.locators.ANDROID_WIDGET_MENU_BUTTON_SHIP_MODE).click()
    # """ - """
    #
    # def play_menu_and_password_to_settings(self):
    #     """Click button MENU and enter password"""
    #     self.element_is_visible(self.locators.BUTTON_MENU).click()
    #     print("CLICk BUTTON MENU")
    #     self.element_is_visible(self.locators.BUTTON_SETTINGS).click()
    #
    # def try_make_screenshot(self, extra_name=''):
    #     self.take_screenshot('my_screen')
    #
    # def try_make_element_screenshot(self, element, extra_name=''):
    #     self.take_element_screenshot(element, 'my_screen_element')
    #
    # def try_check_visible_element(self):
    #     el = self.check_element_is_visible(self.locators.TEXT_VIEW_NO_ACTIVE_DOWNLOADS)
    #
    #     if not el:
    #         self.touch_action(self.locators.BUTTON_FLAG)
    #         self.check_element_is_visible(self.locators.TEXT_VIEW_NO_ACTIVE_DOWNLOADS)
    #
    #     res = self.element_is_visible(self.locators.TEXT_VIEW_NO_ACTIVE_DOWNLOADS)
    #     print(res.text)
    #     self.take_element_screenshot(self.locators.TEXT_VIEW_NO_ACTIVE_DOWNLOADS, 'screen_text')
