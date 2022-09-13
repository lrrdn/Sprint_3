from selenium import webdriver
from selenium.webdriver.common.by import By
import locators
import helpers.auth_helper as helper


class TestUserActions:
    def test_go_to_profile_settings(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.login_to_acc_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.profile_button).click()

        assert driver.find_element(By.XPATH, locators.profile_settings_msg).is_displayed()

        driver.quit()

    def test_go_to_constructor_from_profile_settings(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.login_to_acc_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.profile_button).click()
        driver.find_element(By.XPATH, locators.constructor_button).click()

        assert driver.find_element(By.XPATH, locators.make_order_button).is_displayed()

        driver.quit()

    def test_log_out_from_profile_settings(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.login_to_acc_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.profile_button).click()
        driver.find_element(By.XPATH, locators.log_out_button).click()

        assert driver.find_element(By.XPATH, locators.login_button).is_displayed()

        driver.quit()

    def test_go_to_sauces_tab(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.login_to_acc_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.sauces_tab).click()

        assert driver.find_element(By.XPATH, locators.sauces_menu).is_displayed()

        driver.quit()

    def test_go_to_fillings_tab(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.login_to_acc_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.fillings_tab).click()

        assert driver.find_element(By.XPATH, locators.fillings_menu).is_displayed()

        driver.quit()

    def test_go_to_buns_tab(self):
        driver = webdriver.Chrome()
        helper.open_page(driver)
        driver.find_element(By.XPATH, locators.login_to_acc_button).click()

        helper.sign_in(driver, "lerarodina2972@yandex.ru", "123456")
        driver.find_element(By.XPATH, locators.fillings_tab).click()
        driver.find_element(By.XPATH, locators.buns_tab).click()

        assert driver.find_element(By.XPATH, locators.buns_menu).is_displayed()

        driver.quit()
