from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class AboutPage(BasePage):

    URL = "https://hidr.com.np/"

    WHO_WE_ARE = (
        By.XPATH,
        "//button[normalize-space()='Who We Are']"
    )

    ABOUT_US = (
        By.LINK_TEXT,
        "About Us"
    )

    MAP = (
        By.XPATH,
        "(//div[contains(@class,'group-hover:bg-black/10')])[1]"
    )

    OUR_TEAM = (
        By.LINK_TEXT,
        "Our Team"
    )

    TEAM_CONTENT = (
        By.XPATH,
        "//body/main/div/section/div/div/div[2]/div[1]/div[2]"
    )

    ABOUT_HEADING = (
        By.XPATH,
        "//h1[contains(normalize-space(),'About')]"
    )

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_load()

    def open_about_us(self):

        self.click(self.WHO_WE_ARE)

        element = self.wait_visible(self.ABOUT_US)

        ActionChains(self.driver) \
            .move_to_element(element) \
            .perform()

        element.click()

        self.wait_for_page_load()

    def verify_about_page(self):
        return self.is_visible(self.ABOUT_HEADING)

    def open_map(self):

        self.click(self.WHO_WE_ARE)

        self.click(self.ABOUT_US)

        map_element = self.scroll_to_element(self.MAP)

        ActionChains(self.driver) \
            .move_to_element(map_element) \
            .click() \
            .perform()

    def open_team(self):

        self.click(self.WHO_WE_ARE)

        self.click(self.OUR_TEAM)

        team = self.scroll_to_element(self.TEAM_CONTENT)

        ActionChains(self.driver) \
            .move_to_element(team) \
            .click() \
            .perform()