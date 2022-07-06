# Здесь хранятся проверки со страницы авторизации
import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_url_contains_correct_substring("login"), "Page URL is incorrect! No \'login\' in it."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Не найдена форма логина"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Не найдена форма регистрации"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.NEW_USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.NEW_USER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.NEW_USER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
