from playwright.sync_api import Page

class AdminReportPage:
    """
    Admin report page to search for bookings.
    Implements the same logic as the TypeScript version.
    """
    url: str = "https://automationintesting.online/admin/report"
    # Removed rigid cell selector; just search all events
    event_selector: str = "div.rbc-event-content"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        """Open the admin report page."""
        self.page.goto(self.url)

    def find_booking_in_table(self, full_name: str) -> bool:
        """
        Return True if the booking exists in the report using a flexible event selector.
        Waits a few seconds before checking to ensure events are loaded.
        """
        # Wait a bit for events to load
        self.page.wait_for_timeout(2000)

        # Get all events
        events = self.page.query_selector_all(self.event_selector)
        for event in events:
            text = event.text_content()
            if text and full_name in text:
                return True

        # If not found, return False
        return False

    def logout(self) -> None:
        """Click logout button."""
        logout_selector = "#navbarSupportedContent > ul.navbar-nav.ms-auto > li:nth-child(2) > button"
        self.page.click(logout_selector)
