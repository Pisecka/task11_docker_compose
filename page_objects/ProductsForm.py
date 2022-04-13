from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductsForm(BasePage):
    INPUT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_DESCRIPTION = (
    By.CSS_SELECTOR, "#language1 > div:nth-child(2) > div > div > div.note-editing-area > div.note-editable.panel-body")
    INPUT_META_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    INPUT_META_DESCRIPTION = (By.CSS_SELECTOR, "#input-meta-description1")
    INPUT_META_KEYWORDS = (By.CSS_SELECTOR, "#input-meta-keyword1")
    INPUT_TAGS = (By.CSS_SELECTOR, "#input-tag1")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button")

    def create_product(self, name, description, meta_title, meta_description, meta_keywords, tags):
        self.logger.info('Filling in the Product Form ')
        self._element(self.INPUT_NAME).send_keys(name)
        self._element(self.INPUT_DESCRIPTION).send_keys(description)
        self._element(self.INPUT_META_TITLE).send_keys(meta_title)
        self._element(self.INPUT_META_DESCRIPTION).send_keys(meta_description)
        self._element(self.INPUT_META_KEYWORDS).send_keys(meta_keywords)
        self._element(self.INPUT_TAGS).send_keys(tags)
        self._element(self.BUTTON_SUBMIT).click()