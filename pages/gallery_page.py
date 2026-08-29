from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class GalleryPage(BasePage):

    URL = "https://hidr.com.np/gallery"

    GALLERY_HEADING = (By.XPATH,"//h1[normalize-space()='Gallery']")

    GALLERY_IMAGES = (By.XPATH,"//main//img")

    WHO_WE_ARE = (By.XPATH,"//nav//*[normalize-space()='Who We Are']")

    OPPORTUNITIES = (By.XPATH,"//nav//*[normalize-space()='Opportunities']")

    PUBLICATIONS = (By.XPATH,"//nav//*[normalize-space()='Publications']")

    BLOG = (By.XPATH,"//nav//*[normalize-space()='Blog']")

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_load()

        self.wait_visible(self.GALLERY_HEADING)

    def verify_gallery_page(self):
        return self.is_visible(self.GALLERY_HEADING)

    def get_gallery_images(self):
        return self.driver.find_elements(
            *self.GALLERY_IMAGES
        )

    def hover_gallery_image(self, index=0):

        images = self.get_gallery_images()

        if not images:
            raise AssertionError(
                "No gallery images were found."
            )

        if index >= len(images):
            raise IndexError(
                f"Gallery image index {index} does not exist. "
                f"Total images: {len(images)}"
            )

        image = images[index]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            image
        )

        self.wait.until(
            lambda driver: image.is_displayed()
        )

        ActionChains(self.driver) \
            .move_to_element(image) \
            .pause(1) \
            .perform()

        return image

    def hover_who_we_are(self):
        element = self.wait_visible(self.WHO_WE_ARE)

        ActionChains(self.driver) \
            .move_to_element(element) \
            .pause(1) \
            .perform()

    def hover_opportunities(self):
        element = self.wait_visible(self.OPPORTUNITIES)

        ActionChains(self.driver) \
            .move_to_element(element) \
            .pause(1) \
            .perform()

    def hover_publications(self):
        element = self.wait_visible(self.PUBLICATIONS)

        ActionChains(self.driver) \
            .move_to_element(element) \
            .pause(1) \
            .perform()

    def hover_blog(self):
        element = self.wait_visible(self.BLOG)

        ActionChains(self.driver) \
            .move_to_element(element) \
            .pause(1) \
            .perform()

    def scroll_gallery(self):
        self.driver.execute_script(
            "window.scrollBy(0, 600);"
        )

    def scroll_to_gallery_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )