import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


from pages.base_page import BasePage
from locators.sel_elements_page_locators import ControlSyncWise

from selenium.webdriver import Keys


class ControlSyncWiseSteps(BasePage):
    locators = ControlSyncWise()

    def login_page(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys("123123")
        self.element_is_visible(self.locators.PASSWORD).send_keys("123123")
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()

