import unittest
from selenium import webdriver
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy

class SearchCases(unittest.TestCase):
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

    def test_search_no_element(self):
        self.indexPage.search('Celular')
        self.assertEqual(self.resultPage.get_text(), 'No results were found for your search "Celular"')


    def test_search_element_valid(self):
        self.indexPage.search('Dress')
        self.assertTrue('DRESS' in self.resultPage.return_section_title())


    def test_search_element_valid_two(self):
        self.indexPage.search('T-Shirt')
        self.assertTrue('T-SHIRT' in self.resultPage.return_section_title())

    def test_button_orange(self):
        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_quantity('5')
        self.buyPage.add_elements(3)
        number_of_elements = self.buyPage.get_number_of_elements()
        self.assertEqual(number_of_elements, '8')

    def test_list_product_selection(self):
        self.indexPage.search('T-Shirt')
        self.resultPage.product_list_by_select('Product Name: A to Z')
        self.resultPage.product_list_by_value('reference:desc')
        self.resultPage.product_list_by_index(3)

    #Método con las post-condiciones
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()