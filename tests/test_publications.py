from pages.publication_page import PublicationPage


def test_publications_dropdown(driver):
    publication_page = PublicationPage(driver)

    # Open website
    driver.get(PublicationPage.URL)

    # Hover over Publications
    publication_page.open_publications_menu()

    # Verify dropdown options
    publication_page.verify_dropdown_options()

# verify each option individually



def test_publications_dropdown_options(driver):

    page = PublicationPage(driver)

    driver.get(page.URL)

    # Hover on Publications
    page.open_publications_menu()

    # Report
    assert page.wait.until(
        lambda d: d.find_element(*page.REPORT).is_displayed()
    )

    # Policy Brief
    assert page.wait.until(
        lambda d: d.find_element(*page.POLICY_BRIEF).is_displayed()
    )

    # Annual Report
    assert page.wait.until(
        lambda d: d.find_element(*page.ANNUAL_REPORT).is_displayed()
    )

    # All Publication
    assert page.wait.until(
        lambda d: d.find_element(*page.ALL_PUBLICATION).is_displayed()
    )

    # Book
    assert page.wait.until(
        lambda d: d.find_element(*page.BOOK).is_displayed()
    )

# testing Annual Report:
def test_annual_report_navigation(driver):

    page = PublicationPage(driver)

    driver.get(page.URL)

    # Hover Publications
    page.open_publications_menu()

    # Click Annual Report
    page.click_annual_report()

    # Verify navigation
    page.wait.until(lambda d: d.current_url != PublicationPage.URL)

    assert "annualreport" in driver.current_url.lower()