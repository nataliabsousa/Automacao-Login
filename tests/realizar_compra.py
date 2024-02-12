import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

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
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

driver.find_element(By.XPATH, "//*[@class='btn btn_action btn_medium checkout_button ']").click()
driver.find_element(By.ID, "first-name").send_keys('Natalia')
driver.find_element(By.ID, "last-name").send_keys('Beatriz')
driver.find_element(By.ID, "postal-code").send_keys('11111-311')

driver.find_element(By.ID, "continue").click()
driver.find_element(By.XPATH, "//*[@class='btn btn_action btn_medium cart_button']").click()

assert driver.find_element(By.XPATH, "//*[text()='Thank you for your order!']")

time.sleep(4)
