import time
import pytest
from pages.blog_page import BlogPage


@pytest.mark.parametrize(
    "driver",
    ["chrome", "firefox", "edge"],
    indirect=True
)
def test_hidr_home_navigation(driver):

    Blog_page = BlogPage(driver)

    # Open HIDR website
    driver.get("https://hidr.com.np/")
    time.sleep(3)
    # Verify homepage


    # Click Home
    Blog_page.click_blog(driver)
    time.sleep(3)
