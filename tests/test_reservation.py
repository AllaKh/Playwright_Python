import json
from pages.home_page import HomePage
from pages.admin_page import AdminPage
from pages.room_page import RoomPage
from pages.admin_report_page import AdminReportPage
from playwright.sync_api import Page

def test_full_reservation_flow(page: Page) -> None:
    """
    Full reservation flow: book a room, verify booking in admin report, then logout.
    """
    # Initialize page objects
    home: HomePage = HomePage(page)
    admin: AdminPage = AdminPage(page)
    room: RoomPage = RoomPage(page)
    report: AdminReportPage = AdminReportPage(page)

    # 1. Open home page
    home.open()

    # 2. Go to admin page
    home.go_admin()
    page.wait_for_url("**/admin", timeout=3000)
    assert "/admin" in page.url

    # 3. Login
    admin.login("admin", "password")

    # 4. Back to front page
    home.back_front()
    home.page.wait_for_selector(home.second_room_link, timeout=3000)

    # 5. Scroll down 1/3
    home.scroll_down_one_third()

    # 6. Open second room
    home.open_second_room()
    page.wait_for_url("**/reservation/**", timeout=3000)
    assert "/reservation/" in page.url

    # 7. Wait until heading is visible
    room.page.wait_for_selector(room.heading_selector, timeout=3000)
    assert room.has_heading()

    # 8. Select random dates
    start, end = room.generate_random_dates()

    # Navigate to the reservation page with the generated dates
    room.go_to_room_with_dates(2, start, end)

    page.wait_for_url("**/reservation/**", timeout=3000)
    assert "/reservation/" in page.url

    # 9. Click "Make Reservation"
    room.open_reservation()

    # 10. Load booking payload
    with open("payload.json", "r", encoding="utf-8") as f:
        payload = json.load(f)

    # 11. Fill and submit booking form
    room.fill_booking_form(payload)

    # 12. Wait a moment for confirmation
    page.wait_for_timeout(1000)

    # 13. Go to admin report and check booking
    report.open()
    full_name = f"{payload.get('first_name', '')} {payload.get('last_name', '')}"
    assert report.find_booking_in_table(full_name), f"Booking for {full_name} not found in admin report"

    # 14. Logout
    report.logout()
