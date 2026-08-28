import time

import pytest
from pages.home_page import HomePage
from pages.about_page import AboutPage
from pages.gallery_page import GalleryPage
from pages.opportunity_page import OpportunityPage
from pages.partner_page import PartnerPage


@pytest.mark.e2e
def test_hidr_complete_user_workflow(driver):

    home = HomePage(driver)
    about = AboutPage(driver)
    gallery = GalleryPage(driver)
    opportunity = OpportunityPage(driver)
    partner = PartnerPage(driver)


    #  Open HIDR Homepage


    home.open()

    assert "hidr.com.np" in driver.current_url

    # Verify Explore Our Work is visible
    assert home.is_visible(
        home.EXPLORE_WORK
    )


    # STEP 2 - Explore Our Work


    home.click_explore_work()


    home.wait_visible(
        home.OTHER
    )

    # Apply project filters
    home.filter_projects()


    # STEP 3 - Navigate back Home


    home.click_home_link()

    home.wait_for_page_load()

    assert "hidr.com.np" in driver.current_url


    # # STEP 4 - About Us
    #
    #
    # about.open()
    #
    # about.open_about_us()
    #
    # about.wait_for_page_load()
    #
    # assert about.verify_about_page()
    #
    #
    # # STEP 5 - Our Team
    #
    #
    # about.open()
    #
    # about.open_team()
    #
    # # Verify team section exists
    # assert about.is_visible(
    #     about.TEAM_CONTENT
    # )


    # STEP 6 - Gallery


    gallery.open()

    assert gallery.verify_gallery_page()

    # Verify gallery contains images
    images = gallery.get_gallery_images()

    assert len(images) > 0, \
        "Gallery should contain at least one image"

    # Hover first gallery image
    gallery.hover_gallery_image(index=0)

    # Test navigation hover menus
    gallery.hover_who_we_are()
    gallery.hover_opportunities()
    gallery.hover_publications()
    gallery.hover_blog()

    # Scroll gallery
    gallery.scroll_gallery()

    gallery.scroll_to_gallery_bottom()


    # STEP 7 - Opportunities / Career


    # opportunity.open()

    # opportunity.open_opportunity_workflow()


    # STEP 8 - Partner With Us


    partner.open()
    time.sleep(4)
    partner.click_opportunities()
    time.sleep(4)
    partner.click_partner_with_us()
    time.sleep(4)
    partner.click_contact_us()
    time.sleep(4)

    # STEP 9 - Fill Contact Form


    test_name = "Test User"
    test_email = "testuser@example.com"
    test_phone = "9800000000"
    test_message = "This is an automated Selenium workflow test."

    partner.fill_contact_form(
        name=test_name,
        email=test_email,
        phone=test_phone,
        message=test_message
    )


    # STEP 10 - Validate Form Data


    partner.verify_form_values(
        name=test_name,
        email=test_email,
        phone=test_phone,
        message=test_message
    )


    # STEP 11 - Submit Form


    assert partner.is_visible(
        partner.SEND_BUTTON
    )

    partner.click_send()