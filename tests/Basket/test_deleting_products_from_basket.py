import allure


@allure.epic("Продуктовый магазин")
@allure.feature("Работа с Корзиной")
@allure.title("Проверка очистки формы Корзины до совершения покупки")
def test_deleting_products_from_basket(app):
    with allure.step("Открыть страницу магазина"):
        app.main_page.open_page("")
    with allure.step("Проверить отображение продуктов"):
        app.main_page.viewing_products_list()
    with allure.step("Набрать продуктов в корзину"):
        app.main_page.random_click_on_buying_several_products()
    with allure.step("Открыть корзину"):
        app.main_page.click_basket_icon()
        app.basket_form.basket_form_is_opened()
    with allure.step("Проверить, что в корзине находятся товары"):
        assert app.basket_form.check_shopping_list() != "Cart is Empty"
    with allure.step("Очистить корзину"):
        app.basket_form.delete_all_products_from_basket()
    with allure.step("Проверить успешность очистки корзины"):
        assert app.basket_form.check_shopping_list() == "Cart is Empty"
    with allure.step("Проверить, стоимость товаров в корзине - должно быть 0 руб"):
        assert app.basket_form.get_total_price() == "Total price: 0 ₽"
