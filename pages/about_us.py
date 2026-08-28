from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class AboutUs(object):

    URL = "https://hidr.com.np/"
    Who_We_are = (By.XPATH,"//button[normalize-space()='Who We Are']")
    About_Us = (By.LINK_TEXT,"About Us")
    map = (By.XPATH,"(//div[@class='absolute inset-0 bg-black/0 transition duration-300 group-hover:bg-black/10'])[1]")
    team = (By.LINK_TEXT, "Our Team")
    pra = (By.XPATH,"//body/main/div/section/div/div/div[2]/div[1]/div[2]")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open(self):
        self.driver.get(self.URL)

    def open_about_us(self):
        who = self.wait.until(EC.visibility_of_element_located(self.Who_We_are))
        who.click()
        element = self.wait.until(EC.visibility_of_element_located(self.About_Us))
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    def open_map(self,driver):
        open_map = self.wait.until(EC.visibility_of_element_located(self.map))

        open_map.click()

    def open_team(self,driver):
        self.wait.until(EC.visibility_of_element_located(self.Who_We_are)).click()

        team = self.wait.until(EC.visibility_of_element_located(self.team))
        team.click()


        pra = self.wait.until(EC.visibility_of_element_located(self.pra))
        driver.execute_script("arguments[0].scrollIntoView(true;",pra)
        ActionChains(self.driver).move_to_element(pra).click().perform()

