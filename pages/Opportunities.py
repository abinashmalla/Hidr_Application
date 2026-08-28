from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Opportunity:
    URL = "https://hidr.com.np/"


    OPPORTUNITIES = (By.XPATH,"//button[normalize-space()='Opportunities']")
    CAREER = (By.LINK_TEXT,"Career")
    JOIN_OUR_TEAM = (By.LINK_TEXT,"Join the team")
    MOVE_RIGHT = (By.XPATH,"(//*[name()='path'][@stroke-linecap='round'])[5]")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def wait_for_page_load(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete")

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_load()

    def click_opportunities(self):
        element = self.wait_for_element_clickable(self.OPPORTUNITIES)
        element.click()

    def click_career(self):
        element = self.wait_for_element_clickable(self.CAREER)
        element.click()

    def click_join_our_team(self):
        element = self.wait_for_element_clickable(self.JOIN_OUR_TEAM)
        element.click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",element)

        return element

    def click_move_right(self):
        element = self.scroll_to_element(self.MOVE_RIGHT)
        self.wait.until(EC.element_to_be_clickable(self.MOVE_RIGHT))
        self.driver.execute_script("arguments[0].click();",element)


    def open_opportunity(self):
        self.click_opportunities()
        self.click_career()
        self.click_join_our_team()
        self.scroll_down()
        self.click_move_right()