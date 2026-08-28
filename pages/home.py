import time
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
       self.driver = driver
       self.home = (By.XPATH, "//a[@class='relative rounded-lg px-3 py-2 text-sm transition text-[#F78707]']")
       self.explore_work = (By.XPATH,"//a[normalize-space()='Explore Our Work']")
       self.all_projects = (By.XPATH,"//button[@class='rounded-full px-4 py-2 text-sm font-medium transition-all bg-primary text-primary-foreground']")
       self.other =(By.XPATH,"//button[normalize-space()='Other']")
       self.research = (By.XPATH,"//button[normalize-space()='Research']")
       self.web = (By.XPATH,"//button[normalize-space()='Web']")
       self.Home = (By.LINK_TEXT,"Home")

    def open_url(self, url):
        self.driver.get(url)
        time.sleep(1)

    def click_Home(self):
        self.driver.find_element(*self.home).click()
        time.sleep(2)

    def click_Explore_Work(self):
        self.driver.find_element(*self.explore_work).click()
        time.sleep(2)

    def click_All_projects(self):
        self.driver.find_element(*self.other).click()
        time.sleep(2)
        self.driver.find_element(*self.research).click()
        time.sleep(2)
        self.driver.find_element(*self.web).click()
        time.sleep(2)

    def click_Home1(self):
        self.driver.find_element(*self.Home).click()
        time.sleep(4)