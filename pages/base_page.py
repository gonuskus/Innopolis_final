import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page import MainPageLocator

logger = logging.getLogger()


class BasePage:
    def __init__(self, app):
        self.app = app

    def waiting_open_page(self):
        check_progress_line = self.find_element(MainPageLocator.PROGRESS_LINE)
        wait = WebDriverWait(self.app.wd, 10)
        wait.until(EC.element_selection_state_to_be(check_progress_line, False))

    def find_element(self, locator):
        # time.sleep(0.5)
        return WebDriverWait(self.app.wd, 10).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_clickable_element(self, locator):
        element = WebDriverWait(self.app.wd, 10).until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable {locator}",
        )
        return element

    # def input(self, locator, text):
    #     element = self.find_element(locator)
    #     element.send_keys(text)
    #     return element

    def click_button(self, locator):
        WebDriverWait(self.app.wd, 10).until(
            EC.element_to_be_clickable(locator),
        ).click()

    def open_page(self, open_url):
        self.app.wd.get(self.app.base_url + open_url)
        logger.info(f"Open {self.app.base_url}{open_url}")

    def click_element(self, element):
        element.click()
