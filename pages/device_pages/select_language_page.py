from pages.base_page import AppiumBasePage
from locators.android_locators import SelectLanguageLocators


class SendMessageScreen(AppiumBasePage):

    def select_language(self, number_of_message: int):
        language = self.element_is_visible(SelectLanguageLocators.SELECT_LANGUAGE_BY_NUMBER(number_of_message))
        language_text = language.text
        language.click()
