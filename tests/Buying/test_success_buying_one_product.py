import allure


@allure.epic("Продуктовый магазин")
@allure.feature("Покупка продуктов")
@allure.title("Проверка возможности совершить покупку единственного товара")
def test_success_buying_one_product(app):
    with allure.step("Открыть страницу магазина"):
        app.main_page.open_page("")
    with allure.step("Проверить отображение продуктов"):
        app.main_page.viewing_products_list()
    with allure.step("Набрать продуктов в корзину"):
        app.main_page.random_click_on_buying_one_product()
    with allure.step("Открыть корзину"):
        app.main_page.click_basket_icon()
        app.basket_form.basket_form_is_opened()
    with allure.step("Проверить, что в корзине находятся товары"):
        assert app.basket_form.check_shopping_list() != "Cart is Empty"
    with allure.step("Нажать кнопку покупки"):
        app.basket_form.click_buying_btn()
    with allure.step("Проверить, что появилось сообщение об успешности покупки"):
        assert app.basket_form.check_success_buying_msg() == "Pay done!"
