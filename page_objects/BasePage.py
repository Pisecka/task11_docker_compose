import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging





class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.__create_logger()


    def __create_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.DEBUG)

        f_handler = logging.FileHandler('my_file.log')
        f_handler.setLevel(logging.INFO)
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        self.logger.addHandler(f_handler)

        s_handler = logging.StreamHandler()
        s_handler.setLevel(logging.DEBUG)
        s_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        s_handler.setFormatter(s_format)
        self.logger.addHandler(s_handler)


    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, self.browser.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            self.logger.info('Try to find an element')
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException as exc:
            self.logger.exception(f'RECEIVED ERROR: {exc}')
            # attaching screenshot of the error
            allure.attach(name='error',
                          body=self.browser.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        self.logger.info('Try to click on element')
        element.click()

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    def click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self

    def confirm_alert(self):
        alert = WebDriverWait(self.browser, self.browser.t).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    def _get_browser_url(self):
        self.logger.info('Go to browser URL')
        self.browser.get(self.browser.url)

    def _go_to_catalog_page(self):
        self.logger.info('Go to catalog URL')
        catalog_url = "index.php?route=product/category&path=20"
        self.browser.get(self.browser.url + catalog_url)

    def _go_to_product_page(self):
        self.logger.info('Go to product URL')
        product_url = "index.php?route=product/product&product_id=43"
        self.browser.get(self.browser.url + product_url)

    def _go_to_register_page(self):
        self.logger.info('Go to register URL')
        register_url = "index.php?route=account/register"
        self.browser.get(self.browser.url + register_url)

    def _go_to_admin_page(self):
        self.logger.info('Go to admin URL')
        admin_page = "admin"
        self.browser.get(self.browser.url + admin_page)