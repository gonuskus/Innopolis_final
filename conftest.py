import pytest

from fixtures.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    allure_dir = request.config.getoption("--alluredir")
    headless = request.config.getoption("--headless")
    fixture = Application(base_url, allure_dir, headless)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    ),
    # parser.addoption(
    #     "--alluredir",
    #     action="store",
    #     default="/tmp/allure_results",
    #     help="enter alluredir",
    # ),
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),
