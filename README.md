
# Автоматизированное тестирование Product Shop

[![flake8](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_flake8.yml/badge.svg?branch=main)](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_flake8.yml)
[![pytest](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_pytest.yml/badge.svg?branch=main)](https://github.com/gonuskus/Innopolis_final/actions/workflows/workflow_pytest.yml)
[![Allure](https://img.shields.io/static/v1?label=AllureReport&message=informational&color=blue)](https://gonuskus.github.io/Innopolis_final/)

Реализован проект тестирования [web-портала продуктового магазина](https://berpress.github.io/online-grocery-store/)
Результатом работы автотестирования, является сгенерированный Allure отчет с результатами прогона тестов.


### Инструкция установки и запуска тестов:
### Зависимости проекта:
Для локального запуска проекта необходимо установить Python версии 3.8 и старше.
Далее необходимо установить зависимости проекта тестирования:

```bash
pip3 install -r requirements.txt 
```
Результат выполнения команды - установлены пакеты, требуемые для выполнения тестов.


#### Локальный запуск
Для установки и запуска тестов необходимо [скачать проект](https://github.com/gonuskus/Innopolis_final/archive/refs/heads/main.zip).

Результатом выполнения тестов является Allure отчет.
Для генерации отчета необходимо указать путь к папке, в которой будут храниться файлы.
Папка будет создана в процессе выполнения тестирования.
По умолчанию, отчет будет храниться в проекте тестирования в папке reports

В командной строке перейти в папку проекта и выполнить команду pytest.

Пример команды:
```bash
pytest --alluredir=/reports
```
Результат выполнения команды - выполненные тесты.

Для генерации отчета необходимо вызвать команду ниже и указать путь к папке с отчетами:

```bash
 allure serve /reports
```
Результат выполнения команды - сгенерированный отчет в формате HTML-страницы.

#### Запуск через CI/CD

Автоматизированный прогон возможен средствами GitHub - [GitHub Actions](https://github.com/gonuskus/Innopolis_final/actions)
