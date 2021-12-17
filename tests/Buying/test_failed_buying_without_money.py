import allure


@allure.title("Проверка невозможности покупки при недостаточном балансе")
def test_failed_buying_without_money(app):
    with allure.step("Открыть страницу магазина"):
        pass
    with allure.step("Проверить баланс - должен быть недостаточный"):
        pass
    with allure.step("Набрать продуктов в корзину"):
        pass
    with allure.step("Совершить покупку"):
        pass
    with allure.step("Проверить предупреждение о невозможности покупки"):
        pass
    
