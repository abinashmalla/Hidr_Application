from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PartnerPage(BasePage):

    URL = "https://hidr.com.np/"

    OPPORTUNITIES = (
        By.XPATH,
        "//button[normalize-space()='Opportunities']"
    )

    PARTNER_WITH_US = (
        By.XPATH,
        "//a[normalize-space()='Partner with us']"
    )

    CONTACT_US = (
        By.XPATH,
        "//button[normalize-space()='Contact Us']"
    )

    NAME = (
        By.NAME,
        "name"
    )

    EMAIL = (
        By.NAME,
        "email"
    )

    PHONE = (
        By.NAME,
        "phone"
    )

    MESSAGE = (
        By.NAME,
        "message"
    )

    SEND_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='SEND']"
    )

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_load()

    def click_opportunities(self):
        self.click(self.OPPORTUNITIES)

        self.wait_visible(
            self.PARTNER_WITH_US
        )

    def click_partner_with_us(self):
        self.click(self.PARTNER_WITH_US)

        self.wait_visible(
            self.CONTACT_US
        )

    def click_contact_us(self):
        self.click(self.CONTACT_US)

        self.wait_visible(self.NAME)

    def enter_name(self, name):
        self.enter_text(self.NAME, name)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_phone(self, phone):
        self.enter_text(self.PHONE, phone)

    def enter_message(self, message):
        self.enter_text(self.MESSAGE, message)

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

    def verify_form_values(
        self,
        name,
        email,
        phone,
        message
    ):
        assert self.get_value(self.NAME) == name
        assert self.get_value(self.EMAIL) == email
        assert self.get_value(self.PHONE) == phone
        assert self.get_value(self.MESSAGE) == message

    def click_send(self):
        self.click(self.SEND_BUTTON)