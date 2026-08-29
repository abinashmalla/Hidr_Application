from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OpportunityPage(BasePage):

    URL = "https://hidr.com.np/"

    OPPORTUNITIES = (By.XPATH,"//button[normalize-space()='Opportunities']")

    CAREER = (By.LINK_TEXT,"Career")

    JOIN_OUR_TEAM = (By.LINK_TEXT,"Join the team")

    MOVE_RIGHT = (By.XPATH,"(//*[name()='path'][@stroke-linecap='round'])[5]")

    CAREER_HEADING = (By.XPATH,"//h1[contains(normalize-space(),'Career')]")

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_load()

    def click_opportunities(self):
        self.click(self.OPPORTUNITIES)

    def click_career(self):
        self.click(self.CAREER)

    def click_join_our_team(self):
        self.click(self.JOIN_OUR_TEAM)

    def click_move_right(self):

        element = self.scroll_to_element(self.MOVE_RIGHT)

        self.wait.until(lambda driver: element.is_enabled())

        self.javascript_click(self.MOVE_RIGHT)

    def open_opportunity_workflow(self):

        self.click_opportunities()

        self.click_career()

        self.wait_for_page_load()

        self.click_join_our_team()

        self.wait_for_page_load()

        self.scroll_bottom()

        self.click_move_right()