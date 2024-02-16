import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
# pytest -v -m login
@pytest.mark.login
class TestCT01:
    def testct01_realizarcompra(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce")
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
