# Автотесты для интернет магазина Product Shop

[![code_quality](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_code_quality.yml/badge.svg?branch=main)](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_code_quality.yml)
[![pytest](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_pytest.yml/badge.svg?branch=main)](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_pytest.yml)
[![Allure](https://img.shields.io/static/v1?label=AllureReport&message=informational&color=blue)](https://gonuskus.github.io/Innopolis_final/)
***

Реализован проект тестирования [web-портала продуктового магазина](https://berpress.github.io/online-grocery-store/).

Результатом работы автотестирования, является сгенерированный Allure отчет с результатами прогона тестов проекта.

В рамках данного проекта автоматизированы основные сценарии пользователей:

* работа с корзиной
* поиск товара
* оформление покупки

# Запуск

Указан пример со всеми возможными опциями

```bash
pytest --headless=False
```

# Контроль качества кода

Реализован с помощью pre-commit hook, который проверяет и форматирует код перед коммитом.

## Установка

```
    pip install pre-commit
    pre-commit install
```

## Использование

Хук запускается автоматически перед коммитом. Принудительный запуск:

```
    pre-commit run --all-files
```

# Отчетность выполнения тестов

В проекте подключена отчетность на основе Allure Report для последней версии тестов.

## Просмотр отчётов через CI/CD (GitHub)

После публикации кода тестов будет автоматически сформирован и опубликован отчет тестирования.

Отчет доступен по ссылке - [Allure Report](https://gonuskus.github.io/Innopolis_final/)

## Просмотр отчётов при локальном запуске тестов

### Запуск

```
pytest --alluredir <dir_name>
```

### Просмотр отчёта

```
allure serve <dir_name>
```

# Инструкция установки и запуска тестов

## Установка

1. Создайте отдельную папку на локальном компьютере
2. Скачайте все файлы из [проекта](https://github.com/gonuskus/Innopolis_final)
3. Скачанные файлы переложите в созданную на 1 шаге папку

### Зависимости проекта:

Для локального запуска проекта необходимо установить Python версии 3.8 и старше.

[Подробнее](https://www.python.org/downloads/) об установке можно прочитать на официальном сайте.

Далее необходимо установить зависимости проекта тестирования:

```bash
pip3 install -r requirements.txt
```

Результат выполнения команды будет установка пакетов, требуемых для выполнения тестов. Далее можно запускать тесты.

# CI

Проект подключен к сервису GitHub.

На основе [GitHub Actions](https://github.com/gonuskus/Innopolis_final/actions) реализован код *(.github/workflows)*:

* запуска прогона тестов и подготовки отчетности - workflow_pytest.yml
* проверка качества кода - workflow_code_quality.yml
