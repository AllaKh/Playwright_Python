from playwright.sync_api import Page
from .base_page import BasePage

class AdminPage(BasePage):
    username = "#username"
    password = "#password"
    do_login = "#doLogin"

    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, user: str, pwd: str):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.do_login)
        self.page.wait_for_load_state("networkidle")
