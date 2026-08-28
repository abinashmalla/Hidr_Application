# import time
# from pages.partner_page import PartnerPage
#
#
# def test_Integration(driver):
#     partner_page = PartnerPage(driver)
#     partner_page.open_url("https://hidr.com.np/")
#     driver.maximize_window()
#     time.sleep(2)
#     partner_page.click_opportunities()
#     time.sleep(2)
#     partner_page.click_partner_with_us()
#     time.sleep(2)
#     partner_page.click_contact_us()
#     time.sleep(3)
#
#     partner_page.fill_contact_form(
#         name="Abinash Malla",
#         email="abinashm498@gmail.com",
#         phone="9849658392",
#         message="Testing purpose"
#     )
#
#     partner_page.verify_form_values(
#         name="Abinash Malla",
#         email="abinashm498@gmail.com",
#         phone="9849658392",
#         message="Testing purpose"
#     )
#     time.sleep(3)