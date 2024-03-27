from pages.base_page import AppiumBasePage
from locators.android_locators import SendMessageLocators


class SendMessageScreen(AppiumBasePage):

    def send_message(self, number_of_message: int):
        """Select message"""
        if number_of_message == 8:
            self.swipe_screen_down()
            message = self.element_is_visible(SendMessageLocators.SELECT_MESSAGE_BY_NUMBER(7))
        else:
            message = self.element_is_visible(SendMessageLocators.SELECT_MESSAGE_BY_NUMBER(number_of_message))
        message_text = message.text
        print(message_text)
        message.click()

    def confirm_of_message_sending(self):
        """Press button YES"""
        button_yes = self.element_is_visible(SendMessageLocators.SEND_MESSAGE_BUTTON_YES)
        button_yes.click()

    def cancel_send_message(self):
        """Press button NO"""
        button_no = self.element_is_visible(SendMessageLocators.SEND_MESSAGE_BUTTON_NO)
        button_no.click()

    def leave_send_message_screen(self):
        """Leave send message screen"""
        button_x = self.element_is_visible(SendMessageLocators.SEND_MESSAGE_BUTTON_CANCEL)
        button_x.click()
