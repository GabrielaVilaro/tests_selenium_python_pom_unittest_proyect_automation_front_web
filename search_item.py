import unittest
from selenium import webdriver
import time
from page_index import PageIndex
from page_results import ResultCases

class SearchCases(unittest.TestCase):
    #Método con pre-condiciones
    def setUp(self):
        #instancio mi driver, en este caso chromedriver
        self.driver = webdriver.Chrome('drivers/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemPage = ResultCases(self.driver)
        self.driver.maximize_window()

    def test_search_no_element(self):
        self.indexPage.search('Celular')
        time.sleep(2)
        self.assertEqual(self.itemPage.get_text(), 'No results were found for your search "Celular"')

    def test_search_element_valid(self):
        self.indexPage.search('Dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemPage.return_section_title())

    def test_search_element_valid_two(self):
        self.indexPage.search('T-Shirt')
        time.sleep(2)
        self.assertTrue('T-SHIRT' in self.itemPage.return_section_title())

    #Método con las post-condiciones
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()