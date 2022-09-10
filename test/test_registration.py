import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import helpers.auth_helper as helper
import locators

driver = webdriver.Chrome()


class TestRegistration:
    def test_registration_successful(self):
        helper.sign_up(driver, "Lera", "lerarodina2979@yandex.ru", "123456")

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.quit()

    def test_registration_incorrect_password(self):
        driver.get("https://stellarburgers.nomoreparties.site/")
        helper.sign_up(driver, "Lera", "lerarodina2986@yandex.ru", "123456")

        assert driver.find_element(By.XPATH, locators.incorrect_password_msg).is_displayed()
        driver.quit()
