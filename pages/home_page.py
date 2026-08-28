from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://hidr.com.np/"

    HOME = (
        By.XPATH,
        "//a[contains(@class,'text-[#F78707]')]"
    )

    EXPLORE_WORK = (
        By.XPATH,
        "//a[normalize-space()='Explore Our Work']"
    )

    ALL_PROJECTS = (
        By.XPATH,
        "//button[normalize-space()='All Projects']"
    )

    OTHER = (
        By.XPATH,
        "//button[normalize-space()='Other']"
    )

    RESEARCH = (
        By.XPATH,
        "//button[normalize-space()='Research']"
    )

    WEB = (
        By.XPATH,
        "//button[normalize-space()='Web']"
    )

    HOME_LINK = (
        By.LINK_TEXT,
        "Home"
    )

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_load()
        self.wait_visible(self.EXPLORE_WORK)

    def click_home(self):
        self.click(self.HOME)

    def click_explore_work(self):
        self.click(self.EXPLORE_WORK)

    def filter_projects(self):
        self.click(self.OTHER)
        self.click(self.RESEARCH)
        self.click(self.WEB)

    def click_home_link(self):
        self.click(self.HOME_LINK)