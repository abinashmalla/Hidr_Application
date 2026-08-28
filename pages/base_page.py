from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        element.click()

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        ActionChains(self.driver).move_to_element(element).perform()

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")