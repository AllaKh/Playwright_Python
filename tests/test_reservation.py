import json
from datetime import date, timedelta
from pages.home_page import HomePage
from pages.admin_page import AdminPage
from pages.room_page import RoomPage
from playwright.sync_api import Page

def test_full_reservation_flow(page: Page):
    home = HomePage(page)
    admin = AdminPage(page)
    room = RoomPage(page)

    # Open home
    home.open()

    # Go to admin
    home.go_admin()
    assert "#/admin" in page.url

    # Login
    admin.login("admin", "password")

    # Back to front page
    home.back_front()

    # Check rooms heading
    assert home.has_rooms_heading()

    # Scroll down 1/3
    home.scroll_fraction(0.33)

    # Open second room
    home.open_second_room()

    # Verify room heading present
    assert room.has_heading()

    # Choose dates: tomorrow and tomorrow +10
    start = date.today() + timedelta(days=1)
    end = start + timedelta(days=10)
    page.evaluate("(s, e) => { const startInput = document.querySelector('input[name=start]'); const endInput = document.querySelector('input[name=end]'); if(startInput) startInput.value = s; if(endInput) endInput.value = e; }", start.isoformat(), end.isoformat())

    # Click reservation button
    room.open_reservation()

    # Load payload
    with open('payload.json', 'r', encoding='utf-8') as f:
        payload = json.load(f)

    # Fill and submit booking
    room.fill_booking_form(payload)

    # Wait for confirmation
    page.wait_for_timeout(1000)
    assert page.url.startswith("https://automationintesting.online")
