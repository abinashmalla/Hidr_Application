from pages.annual_report_page import AnnualReportPage


def test_hover_all_annual_report_cards(driver):
    annual_report_page = AnnualReportPage(driver)
    # Action: Open page
    annual_report_page.open_page()
    # Condition: Get Annual Report cards
    cards = annual_report_page.get_report_cards()
    # Assertion: Cards should exist
    assert len(cards) > 0, ("FAIL: No Annual Report cards found."
                            )
    print(f"\nTotal Annual Report cards found: {len(cards)}")
    # Action: Hover over every card
    for index, card in enumerate(cards, start=1):
        annual_report_page.hover_over_card(card)
        # Condition: Card should remain visible
        assert card.is_displayed(), (
            f"FAIL: Annual Report card {index} "
            f"is not visible after hover."
        )
        print(
            f"PASS: Hover successful on "
            f"Annual Report card {index}"
        )