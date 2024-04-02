import time
import pytest

from pages.base_page import BasePage
from locators.web_locators_control import CompanyPageLocators


class CompanyPage(BasePage):
    def select_device_by_device_id(self, device_id):
        row_device = self.element_is_present(CompanyPageLocators.DEVICE_IN_DEVICE_LIST(device_id))
        row_device.click()
