from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Login link is not presented"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        assert EC.alert_is_present, "Should be alert message!"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def check_product_added_message(self, name, price):
        elements = self.browser.find_elements(*ProductPageLocators.ALERT_ADDED)
        name_added = elements[0].text
        price_added = elements[2].text
        assert name_added == name, "Incorrect alert message! Should be {} instead of {}".format(name, name_added)
        assert price_added == price, "Incorrect alert message! Should be {} instead of {}".format(price, price_added)

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message has not disappeared"