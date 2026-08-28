from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class GalleryPage(BasePage):

    URL = "https://hidr.com.np/gallery"
    WHO_WE_ARE = (By.XPATH,"//nav//*[normalize-space()='Who We Are']")
    OPPORTUNITIES = (By.XPATH,"//nav//*[normalize-space()='Opportunities']")
    PUBLICATIONS = (By.XPATH,"//nav//*[normalize-space()='Publications']")
    BLOG = (By.XPATH,"//nav//*[normalize-space()='Blog']")

    #options

    ABOUT_US = (By.XPATH,"//*[normalize-space()='About Us']")

    WHAT_WE_OFFER = (By.XPATH,"//*[normalize-space()='What We Offer']")

    OUR_TEAM = (By.XPATH,"//*[normalize-space()='Our Team']")

    CAREER = (By.XPATH,"//*[normalize-space()='Career']")

    PARTNER_WITH_US = (By.XPATH,"//*[normalize-space()='Partner with us']")

    REPORT = (By.XPATH,"//*[normalize-space()='Report']")

    POLICY_BRIEF = (By.XPATH,"//*[normalize-space()='Policy Brief']")

    ANNUAL_REPORT = (By.XPATH,"//*[normalize-space()='Annual Report']")

    ALL_PUBLICATION = (By.XPATH,"//*[normalize-space()='All Publication']")

    BOOK = (By.XPATH,"//*[normalize-space()='Book']")


    # Gallery


    GALLERY_HEADING = (By.XPATH,"//h1[normalize-space()='Gallery']")

    GALLERY_IMAGES = (By.XPATH,"//main//img")

    #gallery cards
    GALLERY_CARDS = (By.XPATH,"//main//*[self::a or self::article or contains(@class,'card')]")

    # Page actions


    def open(self):
        self.driver.get(self.URL)

        self.wait.until(EC.visibility_of_element_located(self.GALLERY_HEADING))

    def hover_who_we_are(self):
        self.hover(self.WHO_WE_ARE)

    def hover_opportunities(self):
        self.hover(self.OPPORTUNITIES)

    def hover_publications(self):
        self.hover(self.PUBLICATIONS)

    def hover_blog(self):
        self.hover(self.BLOG)

    def get_gallery_images(self):
        return self.get_elements(self.GALLERY_IMAGES)

    def hover_gallery_image(self, index=0):

        images = self.get_gallery_images()

        if index >= len(images):
            raise IndexError(
                f"Gallery image index {index} does not exist. "
                f"Total images: {len(images)}"
            )

        image = images[index]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            image
        )

        self.wait.until(
            EC.visibility_of(image)
        )

        from selenium.webdriver.common.action_chains import ActionChains

        ActionChains(self.driver) \
            .move_to_element(image) \
            .pause(1) \
            .perform()

        return image

    def scroll_gallery(self):
        self.driver.execute_script(
            "window.scrollBy(0, 600);"
        )

    def scroll_to_gallery_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )