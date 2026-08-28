import time
import pytest
from pages.about_us import AboutUs



def test_about_us(driver, wait):
    page = AboutUs(driver, wait)
    time.sleep(2)
    page.open()
    time.sleep(2)
    page.open_about_us()
    time.sleep(2)


def test_map(driver, wait):
    page = AboutUs(driver, wait)
    page.open()
    time.sleep(2)
    page.open_about_us()
    time.sleep(2)
    x = 0
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break
    page.open_map(driver)
    time.sleep(3)