import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.basket_form import BasketForm
from pages.main_page import MainPage

logger = logging.getLogger()


class Application:
    def __init__(self, base_url, report_dir, headless):
        logger.setLevel("INFO")
        options: Options = Options()
        options.headless = headless
        self.create_dir_for_report(report_dir)
        self.wd = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options,
        )
        self.main_page = MainPage(self)
        self.basket_form = BasketForm(self)
        self.base_url = base_url

    def destroy(self):
        logger.info("Quit app")
        self.wd.quit()

    def create_allure_report(self, dir_name):
        cmd = f"allure generate {dir_name} -o {dir_name}/latest --clean"
        code_exit = os.system(cmd)
        logger.info(f"create_allure_report result : {code_exit}")

    @staticmethod
    def create_dir_for_report(dir_name):
        code_exit = os.system(f"rm -rf {dir_name}")
        logger.info(f"Drop old allure files : {code_exit}")
        os.makedirs(f"{dir_name}")
        logger.info(f"Create dir {dir_name}")
