from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[aria-label='submit']")


class CourseMapPageLocators:

    TEXT_MESSAGE = (By.CSS_SELECTOR, "div.contentModal > div:nth-child(1) > div > h5")
    BUTTON_CONFIRMED_MESSAGE = (By.CSS_SELECTOR, "div.contentModal > div.btnwrap > button")
