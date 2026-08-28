import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time




def test_Link_Automation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://hidr.com.np/")
    time.sleep(3)
    link = driver.find_element(By.LINK_TEXT,"Explore Our Work")
    # driver.execute_script("arguments[0].scrollIntoView(true;",link)
    link.click()
    time.sleep(3)
    driver.quit()