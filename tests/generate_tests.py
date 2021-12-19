import allure
import pytest

from tools.actual_products_list import product_list


@allure.epic("Продуктовый магазин")
@allure.feature("Поиск товаров")
@allure.title("Проверка поиска продуктов на сайте магазина")
@pytest.mark.parametrize("product_name", product_list)
def test_success_searching(app, product_name):
    with allure.step("Открыть страницу магазина"):
        app.main_page.open_page("")
    with allure.step("Проверить отображение продуктов"):
        app.main_page.viewing_products_list()
    with allure.step("Вбить в поиск название продукта"):
        app.main_page.searching(product_name)
    with allure.step("Проверить успешность поиска"):
        assert app.main_page.card_content_text() == product_name


# from tools.actual_products_list import product_list
def pytest_generate_tests(app, metafunc):
    product_list = app.main_page.viewing_products_list()
    metafunc.parametrize("product_name", product_list, scope="session")
