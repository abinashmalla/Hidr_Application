import pytest
from pages.Opportunities import Opportunity


def test_open_hidr(driver, wait):
    """
    Verify that HIDR website opens successfully.
    """
    page = Opportunity(driver, wait)

    page.open()

    assert "hidr" in page.driver.current_url.lower()