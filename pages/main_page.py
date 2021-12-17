import logging

from locators.main_page import MainPageLocator
from pages.base_page import BasePage

logger = logging.getLogger()


class MainPage(BasePage):
    def __init__(self, app):
        self.app = app

    def login_name_text(self) -> str:
        return self.login_name().text

    def login_name(self):
        # return self.app.wd.find_element(*Page.LOGIN_NAME)
        return self.find_element(MainPageLocator.LOGIN_NAME)

    def logout_btn(self):
        # return self.app.wd.find_element(MainPageLocator.LOGOUT)
        return self.find_element(MainPageLocator.LOGOUT)

    def logout_user(self):
        self.logout_btn().click()

    def check_auth(self):
        elements = self.find_element(MainPageLocator.LOGIN_NAME)
        return len(elements)
