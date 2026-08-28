import time
import pytest
from pages.hidr_home_page import HidrHomePage




def test_hover_annual_report(driver, wait):
    page = HidrHomePage(driver, wait)
    page.open()
    time.sleep(2)
    page.hover_first_annual_report()
    time.sleep(2)


def test_click_first_annual_report(driver, wait):
    page = HidrHomePage(driver, wait)
    time.sleep(2)
    page.open()
    time.sleep(2)
    page.click_first_annual_report()
    time.sleep(2)


def test_click_second_annual_report(driver, wait):
    page = HidrHomePage(driver, wait)
    time.sleep(2)
    page.open()
    time.sleep(2)
    page.click_second_annual_report()
    time.sleep(2)

def test_click_third_annual_report(driver, wait):
    page = HidrHomePage(driver, wait)
    page.open()
    time.sleep(3)
    page.click_first_annual_report()
    time.sleep(2)
    page.click_second_annual_report()
    time.sleep(2)