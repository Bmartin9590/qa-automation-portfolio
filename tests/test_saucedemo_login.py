from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Login didn’t work—wrong page!"

def test_failed_login(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")
    login_page.login("bad_user", "wrong_pass")
    error = login_page.get_error_message()
    assert "Username and password do not match" in error, f"Expected error, got: '{error}'"