import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)