from pages.gallery_page import GalleryPage


def test_all_navigation_hover(driver):

    gallery_page = GalleryPage(driver)

    gallery_page.open()

    # Who We Are
    gallery_page.hover_who_we_are()

    assert gallery_page.is_visible(
        gallery_page.ABOUT_US
    )

    # Opportunities
    gallery_page.hover_opportunities()

    assert gallery_page.is_visible(
        gallery_page.CAREER
    )

    # Publications
    gallery_page.hover_publications()

    assert gallery_page.is_visible(
        gallery_page.REPORT
    )

    print(
        "\nAll navigation hover actions passed successfully"
    )