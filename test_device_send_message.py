from .pages.main_screen import  MainScreen


def test_first(appium_driver):
    device = MainScreen(appium_driver)
    device.press_button_menu()  # Press button menu

