import pytest

from fixtures.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = "https://berpress.github.io/online-grocery-store/"
    headless = request.config.getoption("--headless")
    report_dir = request.config.getoption("--alluredir")
    fixture = Application(base_url, report_dir, headless)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.destroy()
    fixture.create_allure_report(report_dir)


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),
