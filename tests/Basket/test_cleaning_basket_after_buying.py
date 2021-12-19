import allure


@allure.epic("Продуктовый магазин")
@allure.feature("Работа с Корзиной")
@allure.title("Проверка очистки формы Корзины после совершения покупки")
def test_cleaning_basket_after_buying(app):
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
    with allure.step("Проверить, что корзина очистилась"):
        assert app.basket_form.check_shopping_list() == "Cart is Empty"
    with allure.step(
        "Проверить, стоимость товаров в корзине сбросилась - должно быть 0 руб",
    ):
        assert app.basket_form.get_total_price() == "Total price: 0 ₽"
    with allure.step("Закрыть форму Корзина"):
        app.basket_form.close_basket()
