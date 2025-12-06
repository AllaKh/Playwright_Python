from playwright.sync_api import Page

class AdminReportPage:
    """
    Admin report page to search for bookings.
    Implements the same logic as the TypeScript version.
    """
    url: str = "https://automationintesting.online/admin/report"
    event_selector: str = "#root-container > div > div > div > div > div.rbc-month-view > div:nth-child(2) > div.rbc-row-content > div:nth-child(2) > div:nth-child(2) > div > div.rbc-event-content"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        """Open the admin report page."""
        self.page.goto(self.url)

    def find_booking_in_table(self, full_name: str) -> bool:
        """
        Return True if the booking exists in the report using the exact event selector.
        Waits 2 seconds before checking to ensure events are loaded.
        """
        # Wait 2 seconds for table/events to load
        self.page.wait_for_timeout(2000)

        # Wait for the events to be present
        self.page.wait_for_selector(self.event_selector, timeout=5000)
        events = self.page.query_selector_all(self.event_selector)
        for event in events:
            text = event.text_content()
            if text and full_name in text:
                return True
        return False

    def logout(self) -> None:
        """Click logout button."""
        logout_selector = "#navbarSupportedContent > ul.navbar-nav.ms-auto > li:nth-child(2) > button"
        self.page.click(logout_selector)
