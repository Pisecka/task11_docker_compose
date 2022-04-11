from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    SLIDESHOW = (By.ID, "slideshow0")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "#search > span > button")
    BUTTON_CART = (By.CSS_SELECTOR, "#cart > button")
    SITE_MAP = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(2) > ul > li:nth-child(3) > a")
    CURRENCY = (By.CSS_SELECTOR, "#form-currency > div > button")
    BUTTON_DOLLAR = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > button")

    def click_slideshow(self):
        slideshow = self._element(self.SLIDESHOW)
        self._simple_click_element(slideshow)
        return slideshow

    def click_button_search(self):
        button_search = self._element(self.BUTTON_SEARCH)
        self._simple_click_element(button_search)
        return button_search

    def click_button_cart(self):
        button_cart = self._element(self.BUTTON_CART)
        self._simple_click_element(button_cart)
        return button_cart

    def click_site_map(self):
        site_map = self._element(self.SITE_MAP)
        self._simple_click_element(site_map)
        return site_map

    def click_currency(self):
        currency = self._element(self.CURRENCY)
        self._simple_click_element(currency)
        return currency

    def go_to_catalog_page(self):
        self._go_to_catalog_page()

    def go_to_product_page(self):
        self._go_to_product_page()

    def go_to_register_page(self):
        self._go_to_register_page()

    def go_to_admin_page(self):
        self._go_to_admin_page()

    def click_button_dollar(self):
        button_dollar = self._element(self.BUTTON_DOLLAR)
        self._simple_click_element(button_dollar)
        return button_dollar