from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers.auth_helper as helper
import locators


class TestRegistration:
    def test_registration_successful(self):
        driver = webdriver.Chrome()
        helper.sign_up(driver, "Lera", "lerarodina2960@yandex.ru", "123456")
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.quit()

    def test_registration_incorrect_password(self):
        driver = webdriver.Chrome()
        helper.sign_up(driver, "Lera", "lerarodina2963@yandex.ru", "12345")

        assert driver.find_element(By.XPATH, locators.incorrect_password_msg).is_displayed()
        driver.quit()
