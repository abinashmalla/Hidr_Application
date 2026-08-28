import pytest

from pages.gallery_page import GalleryPage

@pytest.mark.skip(reason="skip test")
def test_gallery_images_displayed(driver):

    gallery_page = GalleryPage(driver)

    gallery_page.open()

    images = gallery_page.get_gallery_images()

    print(f"\nTotal gallery images found: {len(images)}")

    assert len(images) > 0, (
        "No gallery images were found"
    )

    for index, image in enumerate(images, start=1):

        assert image.is_displayed(), (
            f"Gallery image {index} is not displayed"
        )

        print(
            f"Gallery image {index}: displayed successfully"
        )