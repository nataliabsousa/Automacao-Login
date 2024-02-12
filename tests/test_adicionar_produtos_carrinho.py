import pytest
import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.adicionar
class TestCT02:
    def testct02_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory']").click()
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        driver.find_element(By.XPATH, "//*[@class='btn btn_secondary back btn_medium']").click()
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory']").click()
