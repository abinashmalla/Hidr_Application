from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_card_transform(card):

    return card.value_of_css_property("transform")


def get_card_box_shadow(card):

    return card.value_of_css_property("box-shadow")


class AnnualReportPage:

    URL = "https://hidr.com.np/publications/annualreport"

    # Annual Report cards
    REPORT_CARDS = (
        By.CSS_SELECTOR,
        "a[href*='annual-report'], .group"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)

    def open_page(self):

        self.driver.get(self.URL)

    def get_report_cards(self):

        return self.wait.until(
            EC.presence_of_all_elements_located(
                self.REPORT_CARDS
            )
        )

    def scroll_to_card(self, card):

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
            """,
            card
        )

        self.wait.until(
            lambda driver: card.is_displayed()
        )

    def hover_over_card(self, card):
        """Perform hover action on Annual Report card."""

        self.scroll_to_card(card)

        self.wait.until(
            EC.visibility_of(card)
        )

        self.actions.move_to_element(card).pause(1).perform()

    def hover_all_report_cards(self):
        """Hover over all Annual Report cards."""
        cards = self.get_report_cards()

        for index, card in enumerate(cards, start=1):

            self.hover_over_card(card)

            print(
                f"PASS: Hover action performed on "
                f"Annual Report card {index}"
            )

        return cards