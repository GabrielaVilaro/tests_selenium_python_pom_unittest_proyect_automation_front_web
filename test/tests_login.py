import string
import unittest
import random
from selenium import webdriver
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy
from pages.page_sign_in import PageLogin
from pages.page_create_an_account import PageCreateAccount
from pages.page_my_account import PageMyAccount


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
        self.myAccount = PageMyAccount(self.driver)

        # función que genera un email random
        def generate_email(prefix='test123+', domain='gmail.com'):
            random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                                  for _ in range(10))
            return prefix + random_part + '@' + domain

        self.email = generate_email()

    def test_title_of_page(self):
        '''Este test verfica que después de ingresar el mail y presionar el botón crear cuenta, efectivamente
        se pase a la sección AUTHENTICATION'''

        self.indexPage.push_sign_in()
        self.login.send_mail_box(self.email)
        self.login.push_create_an_account()
        self.assertEqual('AUTHENTICATION', self.createdAccount.return_title_of_create_authentication())

    def test_sign_in_complete_verify_name_of_user_and_title_banner_my_account(self):
        '''Este test realiza un registro completo y posteriormente valida que el nombre de usuario
        coincida efectivamente con el creado y que se esté en la página MY ACCOUNT'''

        self.indexPage.push_sign_in()
        self.login.send_mail_box(self.email)
        self.login.push_create_an_account()
        self.createdAccount.select_button_radio_gender()
        self.createdAccount.sender_first_name_and_last_name('Lorena', 'Pérez')
        self.createdAccount.click_in_mail_for_confirmation()
        self.createdAccount.sender_password('Password123')
        self.createdAccount.select_day_month_and_year_with_value('3', '4', '1994')
        self.createdAccount.select_check_box_newsletter()
        self.createdAccount.sender_company_address_and_city('Software', 'América', 'San Martín')
        self.createdAccount.select_state_with_value('12')
        self.createdAccount.sender_postal_code('00000')
        self.createdAccount.select_country_with_value('21')
        self.createdAccount.complete_additional_information('Aditional Information, Great!')
        self.createdAccount.number_phone_mobile_and_home_phone('111111111', '000000000')
        self.createdAccount.sender_address_aditional_alias('This is my address!')
        self.createdAccount.click_button_register()
        name_user_register = self.myAccount.return_text_user_register()
        title_register_successfully = self.myAccount.return_text_of_banner()
        self.assertEqual('Lorena Pérez', name_user_register)
        self.assertTrue('MY ACCOUNT' in title_register_successfully)

    # Método con las post-condiciones
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
