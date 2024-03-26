from pages.base_page import AppiumBasePage
from locators.android_locators import SendMessageLocators


class SendMessageScreen(AppiumBasePage):
    def send_message(self):
        button_menu = self.element_is_visible(SendMessageLocators.FIRST_MESSAGE)
        button_menu.click()
