import time

from pages.base_page import BasePage
from pages.sel_steps_page import ControlSyncWiseSteps


class TestControlSyncWise:
    def test(self, selenium_driver):
        page = ControlSyncWiseSteps(selenium_driver, 'https://control.syncwise360.com/#login')
        page.open()
        time.sleep(3)
        print('Start test')
        page.login_page()
        time.sleep(3)











