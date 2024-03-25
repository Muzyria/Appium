import pytest

from pages.login_page import LoginPage
from pages.main_screen import MainScreen


@pytest.mark.device
def test_first(appium_driver):
    device = MainScreen(appium_driver)
    device.press_button_menu()  # Press button menu


@pytest.mark.web
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_basket(driver, link):
    page = LoginPage(driver, link)      # инициализируем
    page.open()                            # открываем страницу
    page.click_button_add_to_bucket()   # ожидаем, что там нет сообщения об успешном добавлении в корзину
