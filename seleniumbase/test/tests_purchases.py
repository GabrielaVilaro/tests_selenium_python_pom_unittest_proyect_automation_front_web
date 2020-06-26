import unittest
from selenium import webdriver
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy
from pages.page_sign_in import PageLogin
from pages.page_create_an_account import PageCreateAccount
from pages.page_my_account import PageMyAccount

class Purchases(unittest.TestCase):
    #Método con pre-condiciones
    def setUp(self):
        #instancio mi driver, en este caso chromedriver
        self.driver = webdriver.Chrome('../../drivers/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.indexPage = PageIndex(self.driver)
        self.resultPage = ResultCases(self.driver)
        self.buyPage = PageBuy(self.driver)

    def test_product_successfully_added_to_cart_text(self):
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_add_to_cart()
        text_successfully_add_product = self.buyPage.get_text_successfully_add_product_text()
        self.assertTrue(text_successfully_add_product in 'Product successfully added to your shopping cart')


    #Método con las post-condiciones
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()