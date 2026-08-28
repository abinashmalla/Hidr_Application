from pages.gallery_page import GalleryPage


def test_gallery_scroll_and_hover(driver):

    gallery_page = GalleryPage(driver)

    gallery_page.open()

    # Scroll down
    gallery_page.scroll_gallery()

    # Hover first gallery image
    gallery_page.hover_gallery_image(0)

    # Scroll further
    gallery_page.scroll_gallery()

    # Hover second gallery image
    gallery_page.hover_gallery_image(1)

    print(
        "\nGallery scroll and hover actions completed"
    )