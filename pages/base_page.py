import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger()


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator):
        return WebDriverWait(self.app.wd, 10).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    # def page_source(self):
    #     return self.driver.page_source

    def input(self, locator, text: str, wait_time: int = 10) -> WebElement:
        element = self.find_element(locator, wait_time)
        element.send_keys(text)
        return element

    def click_button(self, element):
        element.send_keys(Keys.RETURN)

    def open_page(self, open_url):
        self.app.wd.get(self.app.base_url + open_url)
        logger.info(f'Open {self.app.base_url}{open_url}')

    # def get_title(self) -> str:
    #     return self.driver.title
