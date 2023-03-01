from .base_page import BasePage
from .locators import BasePageLocators
from .locators import CartPageLocators

from selenium.webdriver.common.by import By


class CartPage(BasePage):

    def should_be_no_goods(self):
        assert self.is_not_element_present(*CartPageLocators.GOOD_ITEM), "There are one or more goods in the basket!"

    def should_be_empty_basket_message(self):
        flag = False
        for lang in CartPageLocators.EMPTY_MESSAGES:
            empty_message_loc = "//*[contains(text(), '" + lang + "')]"
            if self.is_element_present(By.XPATH, empty_message_loc):
                flag = True
                return flag
        assert flag, "There no message about empty basket!"
