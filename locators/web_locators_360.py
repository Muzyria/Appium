from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[aria-label='submit']")


class CourseMapPageLocators:
    BUTTON_ASSETS = (By.CSS_SELECTOR, 'button[aria-label="assets"]')

    CART_ASSET_DETAILS = (By.CSS_SELECTOR, "div.tabMenuBtn > ul > li:nth-child(2)")
    LIST_VALUES_ASSET_DETAILS = (By.CSS_SELECTOR, "div.contentInfo > strong")

    MODAL_WINDOW_MESSAGE = (By.CSS_SELECTOR, "div > div.contentModal")
    TEXT_MESSAGE = (By.CSS_SELECTOR, "div.contentModal > div:nth-child(1) > div > h5")
    BUTTON_CONFIRMED_MESSAGE = (By.CSS_SELECTOR, "div.contentModal > div.btnwrap > button")


class AssetsPageLocators:
    @staticmethod
    def CART_IN_LIST_BY_NAME(name):
        return (By.XPATH, f'//td[text()="Car{name}"]')
