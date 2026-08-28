from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PartnerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators
        self.opportunities = (By.XPATH,"//button[normalize-space()='Opportunities']")
        self.partner_with_us = (By.XPATH,"//a[normalize-space()='Partner with us']")
        self.contact_us = (By.XPATH,"//button[normalize-space()='Contact Us']")
        self.name = (By.NAME,"name")
        self.email = (By.NAME,"email")
        self.phone = (By.NAME,"phone")
        self.message = (By.NAME,"message")

        self.send_button = (By.XPATH,"//button[normalize-space()='SEND']")


    def open_url(self, url):
        self.driver.get(url)

        self.wait.until(lambda driver: driver.execute_script("return document.readyState")
                                       == "complete"
        )


    # Generic click method
    def click_element(self, locator):

        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)

        element.click()

        return element


    # Generic input method
    def enter_text(self, locator, text):

        element = self.wait.until(EC.visibility_of_element_located(locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",element)

        self.wait.until(EC.element_to_be_clickable(locator))

        element.clear()
        element.send_keys(text)

        return element


    # Open Opportunities
    def click_opportunities(self):

        self.click_element(self.opportunities)

        self.wait.until( EC.visibility_of_element_located(self.partner_with_us))

    # Click Partner With Us
    def click_partner_with_us(self):

        self.click_element(self.partner_with_us)

        self.wait.until(EC.visibility_of_element_located(self.contact_us))

    # Click Contact Us
    def click_contact_us(self):

        self.click_element(self.contact_us)

        self.wait.until(EC.visibility_of_element_located(self.name))

    # Fill Name

    def enter_name(self, name):

        self.enter_text(self.name,name)

    # Fill Email
    def enter_email(self, email):

        self.enter_text(self.email,email)

    # Fill Phone

    def enter_phone(self, phone):

        self.enter_text(self.phone,phone)

    # Fill Message
    def enter_message(self, message):

        self.enter_text(self.message,message)
    # Fill complete form

    def fill_contact_form(
        self,
        name,
        email,
        phone,
        message
    ):

        self.enter_name(name)

        self.enter_email(email)

        self.enter_phone(phone)

        self.enter_message(message)


    # Verify form values


    def verify_form_values(
        self,
        name,
        email,
        phone,
        message
    ):

        assert self.driver.find_element(
            *self.name
        ).get_attribute("value") == name

        assert self.driver.find_element(
            *self.email
        ).get_attribute("value") == email

        assert self.driver.find_element(
            *self.phone
        ).get_attribute("value") == phone

        assert self.driver.find_element(
            *self.message
        ).get_attribute("value") == message


    # Submit form


    def click_send(self):

        self.click_element(self.send_button)