import unittest
from selenium import webdriver
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy
from pages.page_cart_summary import PageCartSummary

class Purchases(unittest.TestCase):
    #Método con pre-condiciones
    def setUp(self):
        #instancio mi driver, en este caso chromedriver
        self.driver = webdriver.Chrome('../drivers/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.indexPage = PageIndex(self.driver)
        self.resultPage = ResultCases(self.driver)
        self.buyPage = PageBuy(self.driver)
        self.cartSummary = PageCartSummary(self.driver)

    def test_product_successfully_added_to_cart_text(self):
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        text_successfully_add_product = self.buyPage.get_text_successfully_add_product_text()
        self.assertTrue(text_successfully_add_product in 'Product successfully added to your shopping cart')

    def test_title_text_shopping_cart_summary(self):
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        self.buyPage.push_button_proceed_to_checkout()
        text_title_shopping_cart = self.cartSummary.get_text_of_title_shopping_cart()
        self.assertEqual('SHOPPING-CART SUMMARY\nYour shopping cart contains: 1 Product', text_title_shopping_cart)

    def test_number_of_price_total_shopping_cart(self):
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        self.buyPage.push_button_proceed_to_checkout()
        price_total = self.cartSummary.get_number_of_price_total()
        self.assertEqual('$18.51', price_total)


    #Método con las post-condiciones
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()