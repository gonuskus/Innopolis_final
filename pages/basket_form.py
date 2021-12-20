import logging
import time

from selenium.webdriver.remote.webelement import WebElement

from locators.basket_form import BasketFormLocator
from pages.base_page import BasePage

logger = logging.getLogger()


class BasketForm(BasePage):
    def __init__(self, app):
        self.app = app

    def basket_form_is_opened(self):
        self.find_element(BasketFormLocator.BASKET_FORM)

    def check_shopping_list(self):
        time.sleep(1)
        return self.find_element(BasketFormLocator.BASKET_LIST).text

    def get_total_price(self):
        return self.find_element(BasketFormLocator.TOTAL_PRICE).text

    def close_basket(self):
        self.click_element(self.close_basket_button())

    def close_basket_button(self) -> WebElement:
        return self.find_clickable_element(BasketFormLocator.CLOSE_BASKET)

    def delete_all_products_from_basket(self):
        basket_list = self.app.wd.find_elements_by_css_selector(
            "span.secondary-content"
        )
        for i in range(len(basket_list)):
            self.find_element(BasketFormLocator.DELETE_PRODUCT_FROM_BASKET).click()
        logger.info("Вasket has been emptied")

    def check_success_buying_msg(self):
        time.sleep(1)
        return self.find_element(BasketFormLocator.BASKET_MSG).text

    def check_basket_msg(self):
        return self.find_element(BasketFormLocator.BASKET_MSG)

    def click_buying_btn(self):
        # self.click_element(self.buying_button())
        button = self.find_clickable_element(BasketFormLocator.BUY_BTN)
        self.app.wd.execute_script("arguments[0].click();", button)

    def buying_button(self) -> WebElement:
        return self.find_clickable_element(BasketFormLocator.BUY_BTN)
