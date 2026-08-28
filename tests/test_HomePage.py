import time
import pytest
from pages.home import HomePage



def test_Home_Page(driver):
    home_page = HomePage(driver)
    home_page.open_url("https://hidr.com.np/")

    driver.maximize_window()
    home_page.click_Home()
    home_page.click_Explore_Work()
    home_page.click_All_projects()
    x = 0
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break
    home_page.click_Home1()
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break