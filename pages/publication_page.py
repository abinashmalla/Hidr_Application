from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PublicationPage:

    URL = "https://hidr.com.np/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)

    # Main Publications menu
    PUBLICATIONS = (
        By.XPATH,
        "//a[normalize-space()='Publications']"
        " | //button[normalize-space()='Publications']"
    )

    # Dropdown options
    REPORT = (
        By.XPATH,
        "//a[normalize-space()='Report']"
    )

    POLICY_BRIEF = (
        By.XPATH,
        "//a[normalize-space()='Policy Brief']"
    )

    ANNUAL_REPORT = (
        By.XPATH,
        "//a[normalize-space()='Annual Report']"
    )

    ALL_PUBLICATION = (
        By.XPATH,
        "//a[normalize-space()='All Publication']"
    )

    BOOK = (
        By.XPATH,
        "//a[normalize-space()='Book']"
    )

    def open_publications_menu(self):
        """Hover over Publications menu."""
        publications = self.wait.until(
            EC.visibility_of_element_located(self.PUBLICATIONS)
        )

        self.actions.move_to_element(publications).perform()

    def verify_dropdown_options(self):
        """Verify all publication dropdown options are visible."""

        locators = [
            self.REPORT,
            self.POLICY_BRIEF,
            self.ANNUAL_REPORT,
            self.ALL_PUBLICATION,
            self.BOOK
        ]

        for locator in locators:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            assert element.is_displayed()

    def click_report(self):
        self.open_publications_menu()

        report = self.wait.until(
            EC.element_to_be_clickable(self.REPORT)
        )

        report.click()

    def click_policy_brief(self):
        self.open_publications_menu()

        policy_brief = self.wait.until(
            EC.element_to_be_clickable(self.POLICY_BRIEF)
        )

        policy_brief.click()

    def click_annual_report(self):
        self.open_publications_menu()

        annual_report = self.wait.until(
            EC.element_to_be_clickable(self.ANNUAL_REPORT)
        )

        annual_report.click()

    def click_all_publication(self):
        self.open_publications_menu()

        all_publication = self.wait.until(
            EC.element_to_be_clickable(self.ALL_PUBLICATION)
        )

        all_publication.click()

    def click_book(self):
        self.open_publications_menu()

        book = self.wait.until(
            EC.element_to_be_clickable(self.BOOK)
        )

        book.click()