from pages.base_page import AppiumBasePage
from locators.android_locators import SendMessageLocators


class SendMessageScreen(AppiumBasePage):

    def send_message(self):
        list_messages = self.elements_are_visible(SendMessageLocators.FIRST_MESSAGE)
        print(f'elements are visible {len(list_messages)}')
        print()
        for i in list_messages:
            print(i.text)
            # print(i.__dict__)  # Получение значения атрибута 'elementId'


        from appium.webdriver.common.appiumby import By
        message = self.element_is_visible(SendMessageLocators.TEST)
        print(f'---{message.text}')
        message.click()

