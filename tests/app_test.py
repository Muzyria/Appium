import time

from appium.webdriver.common.appiumby import AppiumBy

from pages.app_base_page import BasePage
from locators.app_elements_page_locators import MainScreen


def test(appium_driver):
    # page = BasePage(appium_driver)
    locators = MainScreen()

    el = appium_driver.find_element(locators.BUTTON_MENU)
    el.click()
    time.sleep(3)




# class TestElements:
#     class TestTextBox:
#
#         def test_text_box(self, driver):
#             text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
#             text_box_page.open()
#             full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
#             output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
#             print()
#             assert full_name == output_name, "the full name does not match"
#             assert email == output_email, "the email does not match"
#             assert current_address == output_cur_addr, "the current_address does not match"
#             assert permanent_address == output_per_addr, "the permanent_address does not match"



