import logging
import random

from selenium.webdriver.remote.webelement import WebElement

from locators.main_page import MainPageLocator
from pages.base_page import BasePage

logger = logging.getLogger()


class MainPage(BasePage):
    def __init__(self, app):
        self.app = app

    def viewing_products_list(self):
        products = self.app.wd.find_elements_by_class_name("card-title")
        assert len(products) > 0
        return products

    def _search_input(self):
        return self.find_element(MainPageLocator.SEARCH_FIELD)

    def _search_button(self):
        return self.find_element(MainPageLocator.SEARCH_BTN)

    def searching(self, name_product):
        self._search_input().send_keys(name_product)
        self.click_element(self.submit_button())
        logger.info(f"{name_product} was found")

    def searching_random_product(self):
        products = self.app.wd.find_elements_by_class_name("card-title")
        num_product_card = random.randrange(1, len(products))
        name_product = self.app.wd.find_element_by_css_selector(
            f"div.card:nth-child({num_product_card}) > div:nth-child(2) > span",
        ).text
        self.searching(name_product)
        return name_product

    def error_search_text(self):
        return self.find_element(MainPageLocator.ERROR_SEARCH_TEXT).text

    def submit_button(self) -> WebElement:
        return self.find_clickable_element(MainPageLocator.SEARCH_BTN)

    def card_content_text(self):
        return self.find_element(MainPageLocator.PRODUCT_TITLE).text

    def click_basket_icon(self):
        self.find_clickable_element(MainPageLocator.BASKET_ICON).click()

    def click_buy_btn(self):
        self.find_clickable_element(MainPageLocator.BASKET_ICON).click()

    def random_click_on_buying_several_products(self):
        products = self.app.wd.find_elements_by_class_name("card-title")
        for _ in range(len(products)):
            for i in range(0, random.randint(0, 5)):
                self.app.wd.find_element_by_css_selector(
                    f"div.card:nth-child({_ + 1}) > div:nth-child(3) > button:nth-child(1)",
                ).click()
        logger.info(
            "Several products with different quantities have been added to the cart"
        )

    def random_click_on_buying_one_product(self):
        products = self.app.wd.find_elements_by_class_name("card-title")
        num_product_card = random.randrange(1, len(products))
        for _ in range(0, random.randint(0, 5)):
            self.app.wd.find_element_by_css_selector(
                f"div.card:nth-child({num_product_card}) > div:nth-child(3) > button:nth-child(1)",
            ).click()
        logger.info(
            "Random product with different quantities have been added to the cart"
        )
