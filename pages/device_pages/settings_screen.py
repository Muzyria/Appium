from pages.base_page import AppiumBasePage
from locators.android_locators import SettingsLocators


class SettingsScreen(AppiumBasePage):
    def enter_password(self):
        for number in "123999":
            button = self.element_is_visible(SettingsLocators.BUTTON_NUMBER(number))
            button.click()

        button_submit = self.element_is_visible(SettingsLocators.BUTTON_SUBMIT)
        button_submit.click()

    def press_asset_details_button(self):
        button = self.element_is_visible(SettingsLocators.SELECT_SETTINGS_BY_NUMBER("1"))
        button.click()

    def press_button_cancel(self):
        cancel_button = self.element_is_visible(SettingsLocators.CANCEL_BUTTON)
        cancel_button.click()
