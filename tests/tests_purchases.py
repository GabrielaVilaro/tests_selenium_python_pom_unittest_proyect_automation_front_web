'''Tests realizados para verificar la página de compra de automationpractice.com'''

import unittest
from selenium import webdriver
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy
from pages.page_cart_summary import PageCartSummary
from pages.page_sign_in import PageLogin
from user.user_static import StaticUserRegistered
from pages.base_page import BasePage

__pdoc__ = {}
__pdoc__["TestsPagePurchases"] = False


class TestsPagePurchases(unittest.TestCase):
    '''Método con las pre-condiciones'''

    def setUp(self):
        # instancio mi driver, en este caso chromedriver
        self.basePage = BasePage()
        self.driver = webdriver.Chrome(self.basePage.driver)
        self.driver.get(self.basePage.base_url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.indexPage = PageIndex(self.driver)
        self.resultPage = ResultCases(self.driver)
        self.buyPage = PageBuy(self.driver)
        self.cartSummary = PageCartSummary(self.driver)
        self.login = PageLogin(self.driver)
        self.userStatic = StaticUserRegistered()

    def test_product_successfully_added_to_cart_text(self):
        '''Este tests valida que un producto sea agregado correctamente al carrito de compras'''

        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        text_successfully_add_product = self.buyPage.get_text_successfully_add_product_text()
        self.assertTrue(text_successfully_add_product in 'Product successfully added to your shopping cart')

    def test_title_text_shopping_cart_summary(self):
        '''Este tests verifica título y cantidad de productos agregados al carrito'''

        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        self.buyPage.push_button_proceed_to_checkout()
        text_title_shopping_cart = self.cartSummary.get_text_of_title_shopping_cart()
        self.assertEqual('SHOPPING-CART SUMMARY\nYour shopping cart contains: 1 Product', text_title_shopping_cart)

    def test_number_of_price_total_shopping_cart(self):
        '''Este tests verifica que el precio del producto sea correcto'''

        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        self.buyPage.push_button_proceed_to_checkout()
        price_total = self.cartSummary.get_number_of_price_total()
        self.assertEqual('$19.25', price_total)

    def test_title_text_addresses(self):
        '''Este tests primero ingresa con un usuario válido y después verifica que se pase
        efectivamente a la página ADDRESSES y envía un texto al campo If you would like to add a comment about your
        order, please write it in the field below.'''

        self.indexPage.push_sign_in()
        self.login.send_mail_user_registered(self.userStatic.email_user_registered)
        self.login.send_password_user_registered(self.userStatic.password_user_registered)
        self.login.push_button_sign_in_registered()
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        self.buyPage.push_button_proceed_to_checkout()
        self.cartSummary.push_button_proceed_to_checkout_address()
        self.cartSummary.send_text_in_box_comment_of_address('My adress')
        title_address = self.cartSummary.get_text_of_title_address()
        self.assertEqual('ADDRESSES', title_address)

    def test_page_of_shipping_delivery(self):
        '''Este tests verifica que el título de la sección shipping y el precio de delivery sean correctos'''

        self.indexPage.push_sign_in()
        self.login.send_mail_user_registered(self.userStatic.email_user_registered)
        self.login.send_password_user_registered(self.userStatic.password_user_registered)
        self.login.push_button_sign_in_registered()
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        self.buyPage.push_button_proceed_to_checkout()
        self.cartSummary.push_button_proceed_to_checkout_address()
        self.cartSummary.push_button_proceed_to_checkout_shipping()
        self.cartSummary.click_of_check_box_terms_and_conditions()
        title_of_page = self.cartSummary.get_text_of_title_shipping()
        price_of_delivery = self.cartSummary.get_text_price_of_delivery_shipping()
        self.assertEqual('SHIPPING', title_of_page)
        self.assertEqual('$2.00', price_of_delivery)

    def test_page_of_payment_product_title_and_finally_price_total(self):
        '''Este tests verifica que efectivamete se haya pasado a la página de pago y que el
        precio total sea el correcto'''

        self.indexPage.push_sign_in()
        self.login.send_mail_user_registered(self.userStatic.email_user_registered)
        self.login.send_password_user_registered(self.userStatic.password_user_registered)
        self.login.push_button_sign_in_registered()
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        self.buyPage.push_button_proceed_to_checkout()
        self.cartSummary.push_button_proceed_to_checkout_address()
        self.cartSummary.push_button_proceed_to_checkout_shipping()
        self.cartSummary.click_of_check_box_terms_and_conditions()
        self.cartSummary.push_button_proceed_to_checkout_payment()
        title_payment = self.cartSummary.get_text_of_title_payment()
        price_finally = self.cartSummary.get_text_price_total_finally()
        self.assertEqual('PLEASE CHOOSE YOUR PAYMENT METHOD', title_payment)
        self.assertEqual('$19.25', price_finally)

    ''' Método con las post-condiciones'''

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
