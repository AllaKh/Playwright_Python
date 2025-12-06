from playwright.sync_api import Page
from .base_page import BasePage

class RoomPage(BasePage):
    heading_selector = "#root-container h1"
    do_reservation = "#doReservation"
    booking_input_1 = "#root-container input:nth-of-type(1)"
    booking_input_2 = "#root-container input:nth-of-type(2)"
    booking_input_3 = "#root-container input:nth-of-type(3)"
    booking_input_4 = "#root-container input:nth-of-type(4)"
    submit_button = "#root-container button.btn.btn-primary.w-100.mb-3"

    def __init__(self, page: Page):
        super().__init__(page)

    def has_heading(self) -> bool:
        return self.page.is_visible(self.heading_selector)

    def open_reservation(self):
        self.page.click(self.do_reservation)

    def fill_booking_form(self, payload: dict):
        self.page.fill(self.booking_input_1, payload.get("full_name", ""))
        self.page.fill(self.booking_input_2, payload.get("email", ""))
        self.page.fill(self.booking_input_3, payload.get("phone", ""))
        self.page.fill(self.booking_input_4, payload.get("notes", ""))
        self.page.click(self.submit_button)
