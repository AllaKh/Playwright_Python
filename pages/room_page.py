from playwright.sync_api import Page
from .base_page import BasePage


class RoomPage(BasePage):
    heading_selector: str = "#root-container h1"
    do_reservation: str = "#doReservation"

    # Correct booking form selectors
    booking_input_1: str = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div.input-group.mb-3.room-booking-form > input"  # First Name
    booking_input_2: str = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div:nth-child(2) > input"  # Last Name
    booking_input_3: str = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div:nth-child(3) > input"  # Email
    booking_input_4: str = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div:nth-child(4) > input"  # Phone

    submit_button: str = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > button.btn.btn-primary.w-100.mb-3"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def has_heading(self) -> bool:
        return self.page.is_visible(self.heading_selector)

    def open_reservation(self) -> None:
        self.page.click(self.do_reservation)

    def fill_booking_form(self, payload: dict) -> None:
        self.page.fill(self.booking_input_1, payload.get("first_name", ""))
        self.page.fill(self.booking_input_2, payload.get("last_name", ""))
        self.page.fill(self.booking_input_3, payload.get("email", ""))
        self.page.fill(self.booking_input_4, payload.get("phone", ""))
        self.page.click(self.submit_button)
