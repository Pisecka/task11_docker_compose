from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ProductPage(BasePage):
    PRODUCT_CART = (By.CSS_SELECTOR, "#button-cart")
    REVIEW = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.rating > p > a:nth-child(7)")
    PRODUCT_COMPARE = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.btn-group > button:nth-child(2)")
    PRODUCT_SHARE = (By.CSS_SELECTOR,
                     "#content > div > div.col-sm-4 > div.rating > div > a.addthis_counter.addthis_pill_style.addthis_nonzero > a.atc_s.addthis_button_compact")
    IMAGE_TAP = (By.CSS_SELECTOR, "#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(3) > a > img")

    def go_to_main_page(self):
        self._get_browser_url()

    def click_product_cart(self):
        product_cart = self._element(self.PRODUCT_CART)
        self._simple_click_element(product_cart)
        return product_cart

    def click_review(self):
        review = self._element(self.REVIEW)
        self._simple_click_element(review)
        return review

    def click_product_compare(self):
        product_compare = self._element(self.PRODUCT_COMPARE)
        self._simple_click_element(product_compare)
        return product_compare

    def click_product_share(self):
        product_share = self._element(self.PRODUCT_SHARE)
        self._simple_click_element(product_share)
        return product_share

    def click_image_tap(self):
        image_tap = self._element(self.IMAGE_TAP)
        self._simple_click_element(image_tap)
        return image_tap