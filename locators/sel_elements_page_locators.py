from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """form fields"""
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
