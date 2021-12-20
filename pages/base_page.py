import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page import MainPageLocator

logger = logging.getLogger()


class BasePage:
    def __init__(self, app):
        self.app = app

    def waiting_open_page(self):
        check_progress_line = self.find_element(MainPageLocator.PROGRESS_LINE)
        wait = WebDriverWait(self.app.wd, 10)
        wait.until(
            expected_conditions.element_selection_state_to_be(
                check_progress_line, False
            )
        )
        logger.info("Main page is loaded")

    def find_element(self, locator):
        return WebDriverWait(self.app.wd, 10).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_clickable_element(self, locator):
        return WebDriverWait(self.app.wd, 10).until(
            expected_conditions.element_to_be_clickable(locator),
            message=f"Element not clickable {locator}",
        )

    def open_page(self, open_url):
        self.app.wd.get(self.app.base_url + open_url)
        logger.info(f"Open {self.app.base_url}{open_url}")

    @staticmethod
    def click_element(element):
        element.click()

    def make_screenshot(self):
        logger.info("Screenshot is taken")
        return self.app.wd.get_screenshot_as_png()
