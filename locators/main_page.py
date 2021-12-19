from selenium.webdriver.common.by import By


class MainPageLocator:

    SEARCH_FIELD = (By.ID, "email_inline")

    SEARCH_BTN = (By.TAG_NAME, "button")
    ERROR_SEARCH_TEXT = (By.XPATH, "//h3[contains(text(),'Nothing here, see github')]")
    PROGRESS_LINE = (By.CLASS_NAME, "goods")
    PRODUCT_TITLE = (By.CLASS_NAME, "card-title")

    BASKET_ICON = (By.XPATH, "//i[text()='shopping_cart']")
    BUY_BTN = (By.TAG_NAME, "button")
