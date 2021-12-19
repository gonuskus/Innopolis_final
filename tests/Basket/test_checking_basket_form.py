import allure


@allure.epic("Продуктовый магазин")
@allure.feature("Работа с Корзиной")
@allure.title("Проверка стартового состояния Корзины")
def test_checking_basket_form(app):
    with allure.step("Открыть страницу магазина"):
        app.main_page.open_page("")
    with allure.step(
        "Нажать на иконку 'Корзина' и проверить что отобразилась форма Корзины",
    ):
        app.main_page.click_basket_icon()
        app.basket_form.basket_form_is_opened()
    with allure.step("Проверить, что корзина пустая"):
        assert app.basket_form.check_shopping_list() == "Cart is Empty"
    with allure.step("Проверить, стоимость товаров в корзине - должно быть 0 руб"):
        assert app.basket_form.get_total_price() == "Total price: 0 ₽"
    with allure.step("Закрыть форму Корзина"):
        app.basket_form.close_basket()
