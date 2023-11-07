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

    LIST_APK_VERSION = (By.CSS_SELECTOR, 'div [class="box company-info"] select[name="appVersion"]')

    @staticmethod
    def app_version(text):
        return (By.CSS_SELECTOR, f'select[name="appVersion"] option[value="{text}"]')
    LIST_APK_VERSION_VALUE = (By.CSS_SELECTOR, f'select[name="appVersion"] option[value="2.1.71"]')

    LIST_OS_VERSION = (By.CSS_SELECTOR, 'div [class="box company-info"] select[name="osVersion"]')

    @staticmethod
    def os_version(text):
        return (By.CSS_SELECTOR, f'select[name="osVersion"] option[value="{text}"]')
    LIST_OS_VERSION_VALUE = (By.CSS_SELECTOR, 'select[name="osVersion"] option[value="2.12.0_E"]')



    OTA_VERSION_BUTTON_SAVE = (By.XPATH, '//*[@id="workarea"]/div[2]/section/div[5]/div[2]/div[3]/div[2]/div[2]')

    BUTTON_LOG_OUT = (By.CSS_SELECTOR, '')





