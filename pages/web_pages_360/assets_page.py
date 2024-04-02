from pages.base_page import BasePage
from locators.web_locators_360 import AssetsPageLocators


class AssetsPage(BasePage):
    def select_cart_in_list_by_name(self, name):
        row_cart = self.element_is_visible(AssetsPageLocators.CART_IN_LIST_BY_NAME(name))
        row_cart.click()
