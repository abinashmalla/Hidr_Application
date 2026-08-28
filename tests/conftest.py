import pytest
from selenium import webdriver
from utils import *


@pytest.fixture
def driver():
     options = webdriver.ChromeOptions()
     options.add_argument("--start-maximized")

     driver = webdriver.Chrome(options=options)
     driver.implicitly_wait(5)

     yield driver

     driver.quit()

