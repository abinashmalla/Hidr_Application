from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://hidr.com.np/"

def test_annual_report_hover(driver):
    wait = WebDriverWait(driver, 15)
    driver.get(BASE_URL + "publications/annualreport")
    # Wait until report cards are present
    report_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group")))

    # Make sure at least one report card exists
    assert len(report_cards) > 0, \
        "No Annual Report cards were found."
    print(f"Total Annual Report cards found: {len(report_cards)}")
    # Hover over every report card
    for index, card in enumerate(report_cards, start=1):
    # Scroll card into viewport
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",card)
        # Wait until card is visible
        wait.until(EC.visibility_of(card))

        # Perform hover action
        ActionChains(driver) \
            .move_to_element(card) \
            .pause(1) \
            .perform()

        print(f"Hover performed successfully on report card {index}")

        # Verify the card is still displayed
        assert card.is_displayed(), \
            f"Report card {index} is not displayed after hover."

        # Move mouse away before testing the next card
        ActionChains(driver) \
            .move_by_offset(10, 10) \
            .perform()