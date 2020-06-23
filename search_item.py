import unittest
from selenium import webdriver
import time
from page_index import PageIndex
from page_results import ResultCases
from page_buy import PageBuy

class SearchCases(unittest.TestCase):
    #Método con pre-condiciones
    def setUp(self):
        #instancio mi driver, en este caso chromedriver
        self.driver = webdriver.Chrome('drivers/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemPage = ResultCases(self.driver)
        self.buyPage = PageBuy(self.driver)
        self.driver.maximize_window()

    @unittest.skip
    def test_search_no_element(self):
        self.indexPage.search('Celular')
        time.sleep(2)
        self.assertEqual(self.itemPage.get_text(), 'No results were found for your search "Celular"')

    @unittest.skip
    def test_search_element_valid(self):
        self.indexPage.search('Dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemPage.return_section_title())

    @unittest.skip
    def test_search_element_valid_two(self):
        self.indexPage.search('T-Shirt')
        time.sleep(2)
        self.assertTrue('T-SHIRT' in self.itemPage.return_section_title())

    def test_button_orange(self):
        self.indexPage.search('T-Shirt')
        time.sleep(2)
        self.itemPage.select_color()
        time.sleep(3)
        self.buyPage.push_quantity('5')
        self.buyPage.add_elements(3)
        time.sleep(2)
        number_of_elements = self.buyPage.get_number_of_elements()
        self.assertEqual(number_of_elements, '7')
        time.sleep(3)

    #Método con las post-condiciones
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()