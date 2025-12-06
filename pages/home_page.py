from playwright.sync_api import Page
from .base_page import BasePage

class HomePage(BasePage):
    admin_link = "#navbarNav > ul > li:nth-child(6) > a"
    front_link = "#frontPageLink"
    rooms_h2 = "#rooms > div > div.text-center.mb-5 > h2"
    room_card_button = "#rooms > div > div.row.g-4 > div:nth-child(2) > div > div.card-footer.bg-white.d-flex.justify-content-between.align-items-center > a"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.goto()

    def go_admin(self):
        self.page.click(self.admin_link)

    def back_front(self):
        self.page.click(self.front_link)

    def has_rooms_heading(self) -> bool:
        return self.page.is_visible(self.rooms_h2)

    def open_second_room(self):
        self.page.click(self.room_card_button)
