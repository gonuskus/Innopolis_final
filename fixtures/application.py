import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage

logger = logging.getLogger()


class Application:
    def __init__(self, base_url, allure_dir):
        logger.setLevel('INFO')
        options: Options = Options()
        options.headless = equest.config.getoption("--headless")
        self.create_dir_for_report(allure_dir)
        self.wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.login_page = LoginPage(self)
        self.main_page = MainPage(self)
        self.base_url = base_url

    def destroy(self):
        logger.info('Quit app')
        self.wd.quit()

    def get_url(self):
        return self.wd.current_url

    @staticmethod
    def create_dir_for_report(dir_name):
        if not os.path.exists(dir_name):
            logger.info(f'Create dir {dir_name}')
            os.makedirs(dir_name)
