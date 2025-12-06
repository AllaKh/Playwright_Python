from playwright.sync_api import Page

class AdminReportPage:
    """
    Admin report page to search for bookings.
    """
    url: str = "https://automationintesting.online/admin/report"
    table_selector: str = "#root-container > div > div > div > div > div.rbc-month-view"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        """Open the admin report page."""
        self.page.goto(self.url)

    def find_booking_in_table(self, full_name: str) -> bool:
        """Return True if the booking exists in the table."""
        self.page.wait_for_selector(self.table_selector, timeout=5000)
        cells = self.page.query_selector_all(f"{self.table_selector} div")
        for cell in cells:
            text = cell.text_content()
            if text and full_name in text:
                return True
        return False

    def logout(self) -> None:
        """Click logout button."""
        logout_selector = "#root-container a[href='/admin/logout']"
        self.page.click(logout_selector)
