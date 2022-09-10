import time

from selenium.webdriver.common.by import By
import test.locators as locators


def sign_in(driver, email, password):
    driver.find_element(By.XPATH, locators.register_email_input).send_keys(
        email)
    driver.find_element(By.XPATH, locators.register_password_input).send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, locators.login_button).click()
    driver.implicitly_wait(5)


def sign_up(driver, name, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.login_to_acc_button).click()
    driver.find_element(By.XPATH, locators.register_button).click()

    driver.find_element(By.XPATH, locators.register_name_input).send_keys(name)
    driver.find_element(By.XPATH, locators.register_email_input).send_keys(
        email)
    driver.find_element(By.XPATH, locators.register_password_input).send_keys(password)
    driver.find_element(By.XPATH, locators.register_finish_button).click()
    # implicit and explicit waits don't work on my local machine here
    time.sleep(3)
