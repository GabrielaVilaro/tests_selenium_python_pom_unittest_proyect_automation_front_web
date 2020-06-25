import string
import time
import unittest
import random
from selenium import webdriver
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy
from pages.page_sign_in import PageLogin
from pages.page_create_an_account import PageCreateAccount


class SearchCases(unittest.TestCase):
    # Método con pre-condiciones
    def setUp(self):
        # instancio mi driver, en este caso chromedriver
        self.driver = webdriver.Chrome('../drivers/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.indexPage = PageIndex(self.driver)
        self.itemPage = ResultCases(self.driver)
        self.buyPage = PageBuy(self.driver)
        self.login = PageLogin(self.driver)
        self.createdAccount = PageCreateAccount(self.driver)
        #función que genera un email random
        def generate_email(prefix='huks214+', domain='gmail.com'):
            random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                                  for _ in range(10))
            return prefix + random_part + '@' + domain

        self.email = generate_email()

    def test_email_adress(self):
        self.indexPage.push_sign_in()
        self.login.send_mail_box(self.email)
        self.login.push_create_an_account()
        self.assertEqual('AUTHENTICATION', self.createdAccount.return_title_of_create_authentication())
