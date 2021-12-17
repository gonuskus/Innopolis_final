lint:
	@flake8 .

pytest:
	@pytest -s -v

allure:
	@pytest -s -v

report:
	@allure serve /Users/valentinagonuskus/PycharmProjects/Innopolis_final/reports/allure_results