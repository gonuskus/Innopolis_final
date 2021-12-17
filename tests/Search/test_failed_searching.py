import allure


@allure.title("Проверка поиска несуществующего продукта")
def test_failed_searching(app):
    with allure.step("Открыть страницу магазина"):
        pass
    with allure.step("Проверить отображение продуктов"):
        pass
    with allure.step("Вбить в поиск название продукта"):
        pass
    with allure.step("Проверить отсутствие продукта в поиска"):
        pass
