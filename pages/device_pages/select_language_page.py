from pages.base_page import AppiumBasePage
from locators.android_locators import SelectLanguageLocators


class SelectLanguageScreen(AppiumBasePage):
    def select_language(self, number_of_language: int):
        if number_of_language == 8:
            self.swipe_screen_down()
            language = self.element_is_visible(SelectLanguageLocators.SELECT_LANGUAGE_BY_NUMBER(7))
        else:
            language = self.element_is_visible(SelectLanguageLocators.SELECT_LANGUAGE_BY_NUMBER(number_of_language))
        language_text = language.text
        print(language_text)
        language.click()
