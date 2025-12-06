from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.base_url: str = "https://automationintesting.online/"

    def scroll_to_bottom(self) -> None:
        self.page.evaluate("() => window.scrollBy(0, document.body.scrollHeight)")

    def scroll_to_top(self) -> None:
        self.page.evaluate("() => window.scrollTo(0, 0)")

    def scroll_to_one_third(self) -> None:
        self.page.evaluate("() => window.scrollBy(0, document.body.scrollHeight / 3)")
