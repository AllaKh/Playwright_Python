import json
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.admin_page import AdminPage

def test_admin_login_invalid_passwords(page: Page) -> None:
    """
    Test invalid login attempts for admin page using a list of invalid passwords.
    Each attempt should produce an 'Invalid credentials' error.
    """
    home: HomePage = HomePage(page)
    admin: AdminPage = AdminPage(page)

    # 1. Open home page
    home.open()

    # 2. Go to admin page
    home.go_admin()
    page.wait_for_url("**/admin", timeout=5000)
    assert "/admin" in page.url

    # 3. Load invalid passwords payload
    with open("invalid_passwords.json", "r", encoding="utf-8") as f:
        payload = json.load(f)

    invalid_passwords: list[str] = payload.get("invalidPasswords", [])

    # 4. Selector for login error message
    error_selector: str = "#root-container > div > div > div > div > div.col-sm-8 > div > div.card-body > div"

    # 5. Iterate through invalid passwords and check error
    for pwd in invalid_passwords:
        admin.login("admin", pwd)

        # Wait a short time to allow error message to appear
        page.wait_for_timeout(500)

        # Wait for the error element to appear
        page.wait_for_selector(error_selector, timeout=3000)

        # Check the error text
        error_text: str | None = page.text_content(error_selector)
        assert error_text is not None and "Invalid credentials" in error_text
