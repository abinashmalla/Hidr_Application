from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class HidrHomePage:

    URL = "https://hidr.com.np/"

    FIRST_ANNUAL_REPORT = (By.XPATH,"(//img[@alt='Annual Report 2022'])[1]")
    SECOND_ANNUAL_REPORT = (By.XPATH,"(//img[@alt='Annual Report 2022'])[2]")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open(self):
        self.driver.get(self.URL)

    def hover_first_annual_report(self):
        element = self.wait.until(EC.visibility_of_element_located(self.FIRST_ANNUAL_REPORT))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        ActionChains(self.driver).move_to_element(element).perform()

    def click_first_annual_report(self):
        element = self.wait.until(EC.element_to_be_clickable(self.FIRST_ANNUAL_REPORT))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def click_second_annual_report(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SECOND_ANNUAL_REPORT))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        ActionChains(self.driver).move_to_element(element).click().perform()