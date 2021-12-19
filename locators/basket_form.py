from selenium.webdriver.common.by import By


class BasketFormLocator:
    BASKET_FORM = (By.XPATH, '//li[contains(text(),"Корзина")]')

    BASKET_LIST = (By.CSS_SELECTOR, "li.collection-item:nth-child(2)")
    TOTAL_PRICE = (By.CSS_SELECTOR, "li.collection-item:nth-child(3)")
    BUY_BTN = (By.CSS_SELECTOR, "button.red")
    DELETE_PRODUCT_FROM_BASKET = (By.CLASS_NAME, "basket-delete")

    CLOSE_BASKET = (By.CLASS_NAME, "basket-close")

    BASKET_MSG = (By.XPATH, '//div[contains(text(),"Pay done!")]')
