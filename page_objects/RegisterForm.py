from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterForm(BasePage):
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_PASSWORD2 = (By.CSS_SELECTOR, "#input-confirm")
    PRIVACY_POLICY = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")

    def create_user(self, firstname, lastname, email, telephone, password, password2):
        self.logger.info('Filling in Register Form')
        self._element(self.INPUT_FIRSTNAME).send_keys(firstname)
        self._element(self.INPUT_LASTNAME).send_keys(lastname)
        self._element(self.INPUT_EMAIL).send_keys(email)
        self._element(self.INPUT_TELEPHONE).send_keys(telephone)
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._element(self.INPUT_PASSWORD2).send_keys(password2)
        self._element(self.PRIVACY_POLICY).click()
        self._element(self.BUTTON_SUBMIT).click()