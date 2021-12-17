import logging
import time

from locators.login_page import AuthorizationLocators, RegistrationLocators
from models.login import UserData
from pages.base_page import BasePage

logger = logging.getLogger()


class LoginPage(BasePage):
    def __init__(self, app):
        self.app = app

    def _password_input(self):
        # return self.app.wd.find_element(*Authorization.PASSWORD_INPUT)
        return self.find_element(AuthorizationLocators.PASSWORD_INPUT)

    def _login_input(self):
        # element = (
        #     WebDriverWait(self.app.wd, 10).until(
        #         EC.presence_of_element_located(
        #             Authorization.LOGIN_INPUT))
        # )
        element = self.find_element(AuthorizationLocators.LOGIN_INPUT)
        return element

    def _login_button(self):
        return self.find_element(*AuthorizationLocators.LOGIN_BUTTON)

    # def sign_button_click(self):
    #     self._login_button().click()

    # def _submit_login(self):
    #     return self.app.wd.find_element(*Authorization.SUBMIT_BUTTON)

    def authentication(self, user: UserData):  # , submit=True
        if user.login is not None:
            self._login_input().send_keys(user.login)
        if user.password is not None:
            self._password_input().send_keys(user.password)
        self._login_button().click()

    def error_auth_text(self):
        return self.find_element(AuthorizationLocators.ERROR_AUTH_TEXT).text

    def registration(self, user_data: UserData):
        if user_data.username is not None:
            self._registration_login_input().send_keys(user_data.username)
        if user_data.password is not None:
            self._registration_password_input().send_keys(user_data.password)
        if user_data.email is not None:
            self._registration_email_input().send_keys(user_data.email)
            self._registration_email_dublicate_input().send_keys(user_data.email)
        if user_data.firstname is not None:
            self._registration_firstname_input().send_keys(user_data.firstname)
        if user_data.surname is not None:
            self._registration_surname_input().send_keys(user_data.surname)
        time.sleep(10)
        self._registration_login_button().click()
        logger.info('Sended data for registration')

    def _registration_login_input(self):
        return self.find_element(RegistrationLocators.LOGIN_INPUT)

    def _registration_password_input(self):
        return self.find_element(RegistrationLocators.PASSWORD_INPUT)

    def _registration_email_input(self):
        return self.find_element(RegistrationLocators.EMAIL_INPUT)

    def _registration_email_dublicate_input(self):
        return self.find_element(RegistrationLocators.EMAIL_DUPLICATE_INPUT)

    def _registration_firstname_input(self):
        return self.find_element(RegistrationLocators.FIRSTNAME_INPUT)

    def _registration_surname_input(self):
        return self.find_element(RegistrationLocators.SURNAME_INPUT)

    def _registration_login_button(self):
        return self.find_element(RegistrationLocators.REGISTRATION_BUTTON)

    def success_registration_text(self):
        return self.find_element(RegistrationLocators.REGISTRATION_SUCCESS_TEXT).text

    def error_registration_text(self):
        return self.find_element(RegistrationLocators.REGISTRATION_SUCCESS_TEXT).text

    def error_registration_username_text(self):
        return self.find_element(RegistrationLocators.ERROR_MSG_USERNAME_TEXT).text

    def error_registration_password_text(self):
        return self.find_element(RegistrationLocators.ERROR_MSG_PASSWORD_TEXT).text

    def error_registration_email_text(self):
        return self.find_element(RegistrationLocators.ERROR_MSG_EMAIL_TEXT).text
