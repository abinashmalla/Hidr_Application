import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():

    options = Options()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        options=options
    )

    driver.implicitly_wait(0)

    yield driver

    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)