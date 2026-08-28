from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_page_load(self):
        self.wait.until(
            lambda driver:
            driver.execute_script("return document.readyState") == "complete"
        )

    def wait_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_present(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def scroll_to_element(self, locator):
        element = self.wait_present(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        return element

    def click(self, locator):
        element = self.wait_clickable(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()
        return element

    def javascript_click(self, locator):
        element = self.scroll_to_element(locator)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        return element

    def enter_text(self, locator, text):
        element = self.wait_visible(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.clear()
        element.send_keys(text)

        return element

    def get_value(self, locator):
        element = self.wait_visible(locator)
        return element.get_attribute("value")

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def is_visible(self, locator):
        try:
            return self.wait_visible(locator).is_displayed()
        except Exception:
            return False

    def scroll_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def scroll_top(self):
        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )