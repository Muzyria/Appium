from selenium.webdriver.common.by import By


class ControlSyncWise:
    """Login Page"""
    USER_NAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@id="btn-submit"]')

    FIELD_SEARCH = (By.XPATH, '//input[@class="search"]')

    @staticmethod
    def find_by_text(text):
        return (By.XPATH, f'//*[text()="{text}"]')

    BUTTON_MANAGE_DEVICE = (By.CSS_SELECTOR, 'section[class="horizontal-box stretched-box"] div[class="i"]:nth-child(5)')
    OTA_VERSION_BUTTON_EDIT = (By.CSS_SELECTOR, 'div [class="bt edit"]')





