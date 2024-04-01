from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button#btn-submit")
