# Локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс
from selenium.webdriver.common.by import By


class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME = (By.CSS_SELECTOR, "#content_inner h1")
    ALERT_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.PARTIAL_LINK_TEXT, "basket")

class CartPageLocators(object):
    EMPTY_MESSAGES = {"en" : "Your basket is empty.", "en-gb" : "Your basket is empty.", "ru" : "Ваша корзина пуста"}
    GOOD_ITEM = (By.CLASS_NAME, "basket-items")