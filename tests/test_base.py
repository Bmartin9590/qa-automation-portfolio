def test_saucedemo_title(driver):
    driver.get("https://www.saucedemo.com")
    assert driver.title == "Swag Labs", f"Expected title 'Swag Labs', got '{driver.title}'"