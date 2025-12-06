from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str = "https://automationintesting.online"):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = ""):
        url = self.base_url + path
        self.page.goto(url)

    def scroll_fraction(self, fraction: float = 0.33):
        self.page.evaluate("(fraction) => { window.scrollTo(0, document.body.scrollHeight * fraction); }", fraction)
