from selenium import webdriver
from selenium.webdriver.common.by import By

import helpers.auth_helper as helper
import locators

driver = webdriver.Chrome()


class TestAuth:

    def test_auth_via_login_to_acc_button(self):
        helper.sign_up(driver, "Lera", "lerarodina2972@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.login_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()

    def test_auth_via_profile_button(self):
        helper.sign_up(driver, "Lera", "lerarodina2974@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.profile_button).click()

        helper.sign_in(driver, "lerarodina2974@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()

    def test_auth_via_register_page(self):
        helper.sign_up(driver, "Lera", "lerarodina2971@yandex.ru", "123456")
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, locators.login_from_other_page_button).click()

        helper.sign_in(driver, "lerarodina2971@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()

    def test_auth_via_forgot_password_page(self):
        helper.sign_up(driver, "Lera", "lerarodina2970@yandex.ru", "123456")
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, locators.login_from_other_page_button).click()

        helper.sign_in(driver, "lerarodina2970@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()
