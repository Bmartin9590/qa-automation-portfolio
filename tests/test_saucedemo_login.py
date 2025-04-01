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

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.get_error_message()
    assert "user has been locked out" in error, f"Expected lockout error, got: '{error}'"