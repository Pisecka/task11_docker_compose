import time
import allure

from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.MainPage import MainPage
from page_objects.RegisterPage import RegisterPage
from page_objects.ProductPage import ProductPage

# @allure.suite('MainPage')
# @allure.epic("2022Q1")
# @allure.feature("MainPage")
# @allure.story("slideshow")
# def test_slideshow(browser):
#     slideshow = MainPage(browser).click_slideshow()
#     assert slideshow
#
#
# @allure.suite('MainPage')
# @allure.epic("2022Q1")
# @allure.feature("MainPage")
# @allure.story("button_search")
# def test_search(browser):
#     button_search = MainPage(browser).click_button_search()
#     assert button_search
#
# @allure.suite('MainPage')
# @allure.epic("2022Q1")
# @allure.feature("MainPage")
# @allure.story("button_cart")
# def test_cart(browser):
#     button_cart = MainPage(browser).click_button_cart()
#     assert button_cart
#
#
# @allure.suite('MainPage')
# @allure.epic("2022Q1")
# @allure.feature("MainPage")
# @allure.story("site_map")
# def test_site_map(browser):
#     site_map = MainPage(browser).click_site_map()
#     assert site_map
#
#
# @allure.suite('MainPage')
# @allure.epic("2022Q1")
# @allure.feature("MainPage")
# @allure.story("currency")
# def test_currency(browser):
#     currency = MainPage(browser).click_currency()
#     assert currency
#
# @allure.suite('CatalogPage')
# @allure.epic("2022Q1")
# @allure.feature("CatalogPage")
# @allure.story("sort_catalog")
# def test_catalog_sort(browser):
#     MainPage(browser).go_to_catalog_page()
#     sort_catalog = CatalogPage(browser).click_sort_catalog()
#     assert sort_catalog
#
# @allure.suite('CatalogPage')
# @allure.epic("2022Q1")
# @allure.feature("CatalogPage")
# @allure.story("show_catalog")
# def test_catalog_show(browser):
#     MainPage(browser).go_to_catalog_page()
#     show_catalog = CatalogPage(browser).click_show_catalog()
#     assert show_catalog
#
# @allure.suite('CatalogPage')
# @allure.epic("2022Q1")
# @allure.feature("CatalogPage")
# @allure.story("add_wishlist")
# def test_wishlist(browser):
#     MainPage(browser).go_to_catalog_page()
#     add_wishlist = CatalogPage(browser).click_add_wishlist()
#     assert add_wishlist
#
# @allure.suite('CatalogPage')
# @allure.epic("2022Q1")
# @allure.feature("CatalogPage")
# @allure.story("add_in_cart")
# def test_add_to_cart(browser):
#     MainPage(browser).go_to_catalog_page()
#     add_in_cart = CatalogPage(browser).click_add_in_cart()
#     assert add_in_cart
#
# @allure.suite('CatalogPage')
# @allure.epic("2022Q1")
# @allure.feature("CatalogPage")
# @allure.story("grid_catalog")
# def test_list_catalog(browser):
#     MainPage(browser).go_to_catalog_page()
#     grid_catalog = CatalogPage(browser).click_grid_catalog()
#     assert grid_catalog
#
# @allure.suite('ProductPage')
# @allure.epic("2022Q1")
# @allure.feature("ProductPage")
# @allure.story("product_cart")
# def test_product_in_cart(browser):
#     MainPage(browser).go_to_product_page()
#     product_cart = ProductPage(browser).click_product_cart()
#     assert product_cart
#
# @allure.suite('ProductPage')
# @allure.epic("2022Q1")
# @allure.feature("ProductPage")
# @allure.story("review")
# def test_write_review(browser):
#     MainPage(browser).go_to_product_page()
#     review = ProductPage(browser).click_review()
#     assert review
#
# @allure.suite('ProductPage')
# @allure.epic("2022Q1")
# @allure.feature("ProductPage")
# @allure.story("product_compare")
# def test_compare_product(browser):
#     MainPage(browser).go_to_product_page()
#     product_compare = ProductPage(browser).click_product_compare()
#     assert product_compare
#
# @allure.suite('ProductPage')
# @allure.epic("2022Q1")
# @allure.feature("ProductPage")
# @allure.story("product_share")
# def test_share_product(browser):
#     MainPage(browser).go_to_product_page()
#     product_share = ProductPage(browser).click_product_share()
#     assert product_share
#
# @allure.suite('ProductPage')
# @allure.epic("2022Q1")
# @allure.feature("ProductPage")
# @allure.story("image_tap")
# def test_product_image(browser):
#     MainPage(browser).go_to_product_page()
#     image_tap = ProductPage(browser).click_image_tap()
#     assert image_tap
#
# @allure.suite('RegisterPage')
# @allure.epic("2022Q1")
# @allure.feature("RegisterPage")
# @allure.story("continue_registration")
# def test_registration_continue(browser):
#     MainPage(browser).go_to_register_page()
#     continue_registration = RegisterPage(browser).click_continue_registration()
#     assert continue_registration
#
# @allure.suite('RegisterPage')
# @allure.epic("2022Q1")
# @allure.feature("RegisterPage")
# @allure.story("privacy_policy")
# def test_privacy(browser):
#     MainPage(browser).go_to_register_page()
#     privacy_policy = RegisterPage(browser).click_privacy_policy()
#     assert privacy_policy
#
# @allure.suite('RegisterPage')
# @allure.epic("2022Q1")
# @allure.feature("RegisterPage")
# @allure.story("login_to_page")
# def test_login_page(browser):
#     MainPage(browser).go_to_register_page()
#     login_to_page = RegisterPage(browser).click_login_to_page()
#     assert login_to_page
#
# @allure.suite('RegisterPage')
# @allure.epic("2022Q1")
# @allure.feature("RegisterPage")
# @allure.story("password_forgotten")
# def test_forgot_password(browser):
#     MainPage(browser).go_to_register_page()
#     password_forgotten = RegisterPage(browser).click_password_forgotten()
#     assert password_forgotten
#
# @allure.suite('RegisterPage')
# @allure.epic("2022Q1")
# @allure.feature("RegisterPage")
# @allure.story("to_homepage")
# def test_homepage(browser):
#     MainPage(browser).go_to_register_page()
#     to_homepage = RegisterPage(browser).click_to_homepage()
#     assert to_homepage
#
# @allure.suite('AdminPage')
# @allure.epic("2022Q1")
# @allure.feature("AdminPage")
# @allure.story("admin_login")
# def test_login_admin(browser):
#     MainPage(browser).go_to_admin_page()
#     admin_login = AdminPage(browser).click_admin_login()
#     assert admin_login
#
# @allure.suite('AdminPage')
# @allure.epic("2022Q1")
# @allure.feature("AdminPage")
# @allure.story("admin_login")
# def test_admin_password_forget(browser):
#     MainPage(browser).go_to_admin_page()
#     admin_login = AdminPage(browser).click_admin_password_forget()
#     assert admin_login
#
# @allure.suite('AdminPage')
# @allure.epic("2022Q1")
# @allure.feature("AdminPage")
# @allure.story("catalog_admin")
# def test_admin_catalog(browser):
#     MainPage(browser).go_to_admin_page()
#     admin_login = AdminPage(browser).click_admin_login()
#     catalog_admin = AdminPage(browser).click_catalog_admin()
#     assert catalog_admin
#
# @allure.suite('AdminPage')
# @allure.epic("2022Q1")
# @allure.feature("AdminPage")
# @allure.story("main_page")
# def test_admin_to_main(browser):
#     MainPage(browser).go_to_admin_page()
#     admin_login = AdminPage(browser).click_admin_login()
#     main_page = AdminPage(browser).click_main_page()
#     assert main_page

@allure.suite('AdminPage')
@allure.epic("2022Q1")
@allure.feature("AdminPage")
@allure.story("new_product")
def test_add_new_product_in_admin(browser):
    MainPage(browser).go_to_admin_page()
    time.sleep(2)
    AdminPage(browser).click_admin_login()
    time.sleep(2)
    AdminPage(browser).click_catalog_admin()
    time.sleep(2)
    AdminPage(browser).click_products_link()
    time.sleep(2)
    AdminPage(browser).click_button_plus()
    time.sleep(2)
    AdminPage(browser).fill_new_product_form(name='Test',
                                             description='Test1',
                                             meta_title='Test1',
                                             meta_description='Test1',
                                             meta_keywords='Test1',
                                             tags='test1,my_test1')
    time.sleep(2)
    alert = AdminPage(browser).warning_alert()
    assert alert

@allure.suite('AdminPage')
@allure.epic("2022Q1")
@allure.feature("AdminPage")
@allure.story("delete_product")
def test_delete_product_in_admin(browser):
    MainPage(browser).go_to_admin_page()
    AdminPage(browser).click_admin_login()
    AdminPage(browser).click_catalog_admin()
    AdminPage(browser).click_products_link()
    AdminPage(browser).check_product()
    AdminPage(browser).click_delete_button()
    AdminPage(browser).confirm_alert()
    alert = AdminPage(browser).warning_alert()
    assert alert

@allure.suite('AdminPage')
@allure.epic("2022Q1")
@allure.feature("AdminPage")
@allure.story("register_new_user")
def test_register_new_user(browser):
    MainPage(browser).go_to_register_page()
    AdminPage(browser).fill_register_user_form(firstname='Max',
                                               lastname='Maximov',
                                               email='max@gmail.com',
                                               telephone=555012345,
                                               password='password',
                                               password2='password')
    alert = AdminPage(browser).warning_alert()
    assert alert

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("currency_change")
def test_currency_change(browser):
    MainPage(browser).click_currency()
    button_dollar = MainPage(browser).click_button_dollar()
    assert button_dollar