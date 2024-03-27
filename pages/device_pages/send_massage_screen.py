from pages.base_page import AppiumBasePage
from locators.android_locators import SendMessageLocators


class SendMessageScreen(AppiumBasePage):

    def send_message(self, number_of_message: int):
        message = self.element_is_visible(SendMessageLocators.SELECT_MESSAGE_BY_NUMBER(number_of_message))
        message_text = message.text
        message.click()

    def confirm_of_message_sending(self):
        button_yes = self.elements_are_visible(SendMessageLocators.SEND_MESSAGE_BUTTON_YES)
        button_yes.click()

    def cancel_send_message(self):
        button_no = self.elements_are_visible(SendMessageLocators.SEND_MESSAGE_BUTTON_NO)
        button_no.click()



