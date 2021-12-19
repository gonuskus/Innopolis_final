import allure


@allure.epic("Продуктовый магазин")
@allure.feature("Поиск товаров")
@allure.title("Проверка поиска продуктов на сайте магазина")
def test_success_searching(app):
    with allure.step("Открыть страницу магазина"):
        app.main_page.open_page("")
    with allure.step("Проверить отображение продуктов"):
        app.main_page.viewing_products_list()
    with allure.step("Вбить в поиск название продукта"):
        searching_product = app.main_page.searching_random_product()
    with allure.step("Проверить успешность поиска"):
        assert app.main_page.card_content_text() == searching_product
