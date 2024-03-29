from pages.base_page import AppiumBasePage
from locators.android_locators import MenuScreenLocators


class MenuScreen(AppiumBasePage):
    def press_button_play_golf(self):
        button_menu = self.element_is_visible(MenuScreenLocators.BUTTON_PLAY_GOLF)
        button_menu.click()

    def press_button_send_message(self):
        button_send_message = self.element_is_visible(MenuScreenLocators.BUTTON_SEND_MESSAGE)
        button_send_message.click()

