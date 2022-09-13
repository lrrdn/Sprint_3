from selenium import webdriver
from selenium.webdriver.common.by import By

import helpers.auth_helper as helper
import locators


class TestAuth:

    def test_auth_via_login_to_acc_button(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.login_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()

    def test_auth_via_profile_button(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.profile_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()

    def test_auth_via_register_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, locators.login_from_other_page_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()

    def test_auth_via_forgot_password_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, locators.login_from_other_page_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()
