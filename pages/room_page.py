import random
from datetime import datetime, timedelta
from playwright.sync_api import Page

class RoomPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading_selector = "#root-container h1"
        self.do_reservation_selector = "#doReservation"

        # Booking form inputs
        self.first_name_input = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div.input-group.mb-3.room-booking-form > input"
        self.last_name_input = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div:nth-child(2) > input"
        self.email_input = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div:nth-child(3) > input"
        self.phone_input = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > div:nth-child(4) > input"
        self.submit_button = "#root-container > div > div.container.my-5 > div > div.col-lg-4 > div > div > form > button.btn.btn-primary.w-100.mb-3"

    def has_heading(self) -> bool:
        return self.page.locator(self.heading_selector).is_visible()

    # ================= RANDOM DATES =================
    def generate_random_dates(self):
        """
        Generate random check-in and check-out dates
        """
        offset = random.randint(0, 9)
        checkin = datetime.now() + timedelta(days=offset)
        checkout = checkin + timedelta(days=1)
        return checkin.strftime("%Y-%m-%d"), checkout.strftime("%Y-%m-%d")

    def go_to_room_with_dates(self, room_id: int, checkin: str, checkout: str):
        """
        Navigate directly to reservation URL with dates
        """
        url = f"https://automationintesting.online/reservation/{room_id}?checkin={checkin}&checkout={checkout}"
        self.page.goto(url)

    # ================= RESERVATION =================
    def open_reservation(self):
        """
        Click 'Make Reservation' button on sidebar
        """
        self.page.locator(self.do_reservation_selector).click()

    def fill_booking_form(self, payload: dict):
        self.page.locator(self.first_name_input).fill(payload.get("first_name", ""))
        self.page.locator(self.last_name_input).fill(payload.get("last_name", ""))
        self.page.locator(self.email_input).fill(payload.get("email", ""))
        self.page.locator(self.phone_input).fill(payload.get("phone", ""))
        self.page.locator(self.submit_button).click()
