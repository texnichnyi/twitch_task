import pytest

from base.driver import Driver
from pages.home import Home


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android")


@pytest.fixture(scope='function')
def get_home_page(request):
    """
    Setup and delete driver
    :return: driver
    """
    driver = Driver(platform=request.config.option.platform)
    home_page = Home(driver.get_driver())
    yield home_page
    driver.close_driver()
    del driver



