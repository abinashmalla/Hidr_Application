from pages.gallery_page import GalleryPage


def test_gallery_hover_css_change(driver):

    gallery_page = GalleryPage(driver)

    gallery_page.open()

    images = gallery_page.get_gallery_images()

    image = images[0]

    before_transform = image.value_of_css_property(
        "transform"
    )

    gallery_page.hover_gallery_image(0)

    after_transform = image.value_of_css_property(
        "transform"
    )

    print(
        f"\nBefore hover transform: {before_transform}"
    )

    print(
        f"After hover transform: {after_transform}"
    )