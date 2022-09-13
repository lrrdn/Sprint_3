from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import test.locators as locators
from selenium.webdriver.support.wait import WebDriverWait


def open_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")


def sign_in(driver, email, password):
    driver.find_element(By.XPATH, locators.register_email_input).send_keys(
        email)
    driver.find_element(By.XPATH, locators.register_password_input).send_keys(password)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button)))
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.make_order_button)))


def sign_up(driver, name, email, password):
    open_page(driver)
    driver.find_element(By.XPATH, locators.login_to_acc_button).click()
    driver.find_element(By.XPATH, locators.register_button).click()

    driver.find_element(By.XPATH, locators.register_name_input).send_keys(name)
    driver.find_element(By.XPATH, locators.register_email_input).send_keys(
        email)
    driver.find_element(By.XPATH, locators.register_password_input).send_keys(password)
    driver.find_element(By.XPATH, locators.register_finish_button).click()
