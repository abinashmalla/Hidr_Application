from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


class BlogPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    blog = (By.LINK_TEXT,"Blog")
    load_more = (By.XPATH,"//button[normalize-space()='Load More']")
    read_more = (By.XPATH,"(//article//a[normalize-space()='Read More'])[6]")

    def click_blog(self, driver):
       blog = self.wait.until(EC.element_to_be_clickable(self.blog))
       blog.click()

       x = 0
       while True:
           x += 1
           driver.execute_script("scrollBy(0,50)")
           time.sleep(0.10)
           if x > 100:
               break
       element = self.wait.until(EC.element_to_be_clickable(self.load_more))
       element.click()
       time.sleep(3)
       self.wait.until(EC.element_to_be_clickable(self.read_more)).click()
       time.sleep(4)