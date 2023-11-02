import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


from pages.base_page import BasePage
from locators.sel_elements_page_locators import *

from selenium.webdriver import Keys

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        return full_name
