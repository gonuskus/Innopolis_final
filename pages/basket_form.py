import logging
import time

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
        self.find_clickable_element(BasketFormLocator.CLOSE_BASKET).click()

    def delete_all_products_from_basket(self):
        basket_list = self.app.wd.find_elements_by_css_selector(
            "span.secondary-content",
        )
        for i in range(0, len(basket_list)):
            self.app.wd.find_element_by_xpath(
                f"/html/body/div/div/main/ui/li[{1 + 1}]/span/i",
            ).click()

    def check_success_buying_msg(self):
        time.sleep(1)
        return self.find_element(BasketFormLocator.BASKET_MSG).text

    def check_basket_msg(self):
        return self.find_element(BasketFormLocator.BASKET_MSG)

    def click_buying_btn(self):
        self.find_clickable_element(BasketFormLocator.BUY_BTN).click()