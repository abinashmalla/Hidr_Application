import pytest
from pages.gallery_page import GalleryPage



def test_gallery_page_loads(driver):

    page = GalleryPage(driver)
    page.open()
    assert page.is_visible(page.GALLERY_HEADING)

    assert driver.current_url == page.URL

@pytest.mark.skip(reason="Not implemented")
def test_gallery_images_displayed(driver):

    page = GalleryPage(driver)
    page.open()
    images = page.get_gallery_images()
    print(f"\nTotal gallery images: {len(images)}")

    assert len(images) > 0

    for image in images:
      assert image.is_displayed()


def test_who_we_are_hover(driver):

    page = GalleryPage(driver)
    page.open()
    page.hover_who_we_are()

    assert page.is_visible(page.ABOUT_US)

    assert page.is_visible(page.WHAT_WE_OFFER)

    assert page.is_visible(page.OUR_TEAM)


def test_opportunities_hover(driver):

    page = GalleryPage(driver)
    page.open()
    page.hover_opportunities()

    assert page.is_visible(page.CAREER)

    assert page.is_visible(page.PARTNER_WITH_US)


def test_publications_hover(driver):

    page = GalleryPage(driver)
    page.open()
    page.hover_publications()

    assert page.is_visible(page.REPORT)

    assert page.is_visible(page.POLICY_BRIEF)

    assert page.is_visible(page.ANNUAL_REPORT)

    assert page.is_visible(page.ALL_PUBLICATION)

    assert page.is_visible(page.BOOK)


def test_gallery_hover(driver):

    page = GalleryPage(driver)
    page.open()
    images = page.get_gallery_images()
    assert len(images) > 0
    for index in range(min(len(images), 6)):

     page.hover_gallery_image(index)
     print(f"Hovered gallery image: {index + 1}")


def test_gallery_scroll(driver):

    page = GalleryPage(driver)
    page.open()
    page.scroll_gallery()
    page.scroll_gallery()
    page.scroll_to_gallery_bottom()

    print("\nGallery scrolling completed successfully")