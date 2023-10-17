import time

from appium.webdriver.common.appiumby import AppiumBy

from pages.app_base_page import BasePage


def test(appium_driver):
    page = BasePage(appium_driver)

    el = appium_driver.find_element(by=AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
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



