from selenium.webdriver.common.by import By

from .BasePage import BasePage


class CatalogPage(BasePage):
    SORT_CATALOG = (By.CSS_SELECTOR, "#input-sort")
    SHOW_CATALOG = (By.CSS_SELECTOR, "#input-limit")
    ADD_WISHLIST = (By.CSS_SELECTOR,
                    "#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(2)")
    ADD_IN_CART = (By.CSS_SELECTOR,
                   "#content > div:nth-child(7) > div:nth-child(2) > div > div:nth-child(2) > div.button-group > button:nth-child(1)")
    GRID_CATALOG = (By.CSS_SELECTOR, "#grid-view")

    def go_to_main_page(self):
        self._get_browser_url()

    def click_sort_catalog(self):
        sort_catalog = self._element(self.SORT_CATALOG)
        self._simple_click_element(sort_catalog)
        return sort_catalog

    def click_show_catalog(self):
        show_catalog = self._element(self.SHOW_CATALOG)
        self._simple_click_element(show_catalog)
        return show_catalog

    def click_add_wishlist(self):
        add_wishlist = self._element(self.ADD_WISHLIST)
        self._simple_click_element(add_wishlist)
        return add_wishlist

    def click_add_in_cart(self):
        add_in_cart = self._element(self.ADD_IN_CART)
        self._simple_click_element(add_in_cart)
        return add_in_cart

    def click_grid_catalog(self):
        grid_catalog = self._element(self.GRID_CATALOG)
        self._simple_click_element(grid_catalog)
        return grid_catalog
