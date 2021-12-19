import allure


@allure.epic("Продуктовый магазин")
@allure.feature("Поиск товаров")
@allure.title("Проверка поиска несуществующего продукта")
def test_failed_searching(app):
    with allure.step("Открыть страницу магазина"):
        app.main_page.open_page("")
    with allure.step("Проверить отображение продуктов"):
        app.main_page.viewing_products_list()
    with allure.step("Вбить в поиск название продукта"):
        app.main_page.searching("SUP")
    with allure.step("Проверить отсутствие продукта в поиска"):
        assert app.main_page.error_search_text() == "Nothing here, see github"
