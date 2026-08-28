import pytest

from pages.home_page import HomePage
from pages.about_page import AboutPage
from pages.gallery_page import GalleryPage
from pages.opportunity_page import OpportunityPage
from pages.partner_page import PartnerPage


@pytest.mark.e2e
def test_homepage_workflow(driver):

    page = HomePage(driver)

    page.open()

    assert page.is_visible(
        page.EXPLORE_WORK
    )

    page.click_explore_work()

    page.filter_projects()

    page.click_home_link()


@pytest.mark.e2e
def test_about_us_workflow(driver):

    page = AboutPage(driver)

    page.open()

    page.open_about_us()

    assert page.verify_about_page()


@pytest.mark.e2e
def test_our_team_workflow(driver):

    page = AboutPage(driver)

    page.open()

    page.open_team()

    assert page.is_visible(
        page.TEAM_CONTENT
    )


@pytest.mark.e2e
def test_gallery_workflow(driver):

    page = GalleryPage(driver)

    page.open()

    assert page.verify_gallery_page()

    images = page.get_gallery_images()

    assert len(images) > 0

    page.hover_gallery_image(0)

    page.hover_who_we_are()
    page.hover_opportunities()
    page.hover_publications()
    page.hover_blog()

    page.scroll_gallery()
    page.scroll_to_gallery_bottom()


@pytest.mark.e2e
def test_opportunity_workflow(driver):

    page = OpportunityPage(driver)

    page.open()

    page.open_opportunity_workflow()


@pytest.mark.e2e
def test_partner_contact_workflow(driver):

    page = PartnerPage(driver)

    page.open()

    page.click_opportunities()
    page.click_partner_with_us()
    page.click_contact_us()

    page.fill_contact_form(
        "Test User",
        "testuser@example.com",
        "9800000000",
        "Automated Selenium test message."
    )

    page.verify_form_values(
        "Test User",
        "testuser@example.com",
        "9800000000",
        "Automated Selenium test message."
    )

    assert page.is_visible(
        page.SEND_BUTTON
    )