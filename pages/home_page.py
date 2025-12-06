from playwright.sync_api import Page
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.admin_link: str = "#navbarNav > ul > li:nth-child(6) > a"
        self.second_room_link: str = "#rooms > div > div.row.g-4 > div:nth-child(2) > div > div.card-footer.bg-white.d-flex.justify-content-between.align-items-center > a"

    def open(self) -> None:
        self.page.goto(self.base_url)

    def go_admin(self) -> None:
        self.page.click(self.admin_link)

    def back_front(self) -> None:
        self.page.click("#frontPageLink")

    def scroll_down_one_third(self) -> None:
        self.scroll_to_one_third()

    def open_second_room(self) -> None:
        self.page.wait_for_selector(self.second_room_link, state="visible", timeout=5000)
        self.page.locator(self.second_room_link).click(force=True)
