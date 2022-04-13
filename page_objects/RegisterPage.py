from selenium.webdriver.common.by import By

from .BasePage import BasePage


class RegisterPage(BasePage):
    CONTINUE_REGISTRATION = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
    PRIVACY_POLICY = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")
    LOGIN_TO_PAGE = (By.CSS_SELECTOR, "#content > p > a")
    PASSWORD_FORGOTTEN = (By.CSS_SELECTOR, "#column-right > div > a:nth-child(3)")
    TO_HOMEPAGE = (By.CSS_SELECTOR, "#account-register > ul > li:nth-child(1) > a > i")

    def go_to_main_page(self):
        self._get_browser_url()

    def click_continue_registration(self):
        continue_registration = self._element(self.CONTINUE_REGISTRATION)
        self._simple_click_element(continue_registration)
        return continue_registration

    def click_privacy_policy(self):
        privacy_policy = self._element(self.PRIVACY_POLICY)
        self._simple_click_element(privacy_policy)
        return privacy_policy

    def click_login_to_page(self):
        login_to_page = self._element(self.LOGIN_TO_PAGE)
        self._simple_click_element(login_to_page)
        return login_to_page

    def click_password_forgotten(self):
        password_forgotten = self._element(self.PASSWORD_FORGOTTEN)
        self._simple_click_element(password_forgotten)
        return password_forgotten

    def click_to_homepage(self):
        to_homepage = self._element(self.TO_HOMEPAGE)
        self._simple_click_element(to_homepage)
        return to_homepage