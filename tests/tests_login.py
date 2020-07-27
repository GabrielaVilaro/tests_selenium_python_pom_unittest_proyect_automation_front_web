"""Tests para verificar la página de login de automationpractice.com"""

import unittest
from selenium import webdriver
from functions.functions import FunctionsUtils
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy
from pages.page_sign_in import PageLogin
from pages.page_create_an_account import PageCreateAccount
from pages.page_my_account import PageMyAccount
from user.user_static import StaticUserSigIn
from pages.base_page import BasePage

__pdoc__ = {}
__pdoc__["TestsPageLogin"] = False


class TestsPageLogin(unittest.TestCase):
    """Método con las pre-condiciones"""

    @classmethod
    def setUpClass(cls):
        cls.basePage = BasePage()
        cls.driver = webdriver.Chrome(cls.basePage.driver)
        cls.driver.get(cls.basePage.base_url)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.login = PageLogin(cls.driver)
        cls.indexPage = PageIndex(cls.driver)
        cls.itemPage = ResultCases(cls.driver)
        cls.buyPage = PageBuy(cls.driver)
        cls.createdAccount = PageCreateAccount(cls.driver)
        cls.myAccount = PageMyAccount(cls.driver)
        cls.utilsFunctions = FunctionsUtils()
        cls.userStatic = StaticUserSigIn()

    def test_title_of_page(self):
        """Este tests verfica que después de ingresar el mail y presionar el botón crear cuenta, efectivamente
        se pase a la sección AUTHENTICATION"""

        self.indexPage.push_sign_in()
        self.login.send_mail_box(self.utilsFunctions.generate_email())
        self.login.push_create_an_account()
        self.assertEqual('AUTHENTICATION', self.createdAccount.return_title_of_create_authentication())

    def test_sign_in_complete_verify_name_of_user_and_title_banner_my_account(self):
        """Este tests realiza un registro completo y posteriormente valida que el nombre de usuario
        coincida efectivamente con el creado y que se esté en la página MY ACCOUNT"""

        self.indexPage.push_sign_in()
        self.login.send_mail_box(self.utilsFunctions.generate_email())
        self.login.push_create_an_account()
        self.createdAccount.select_button_radio_gender()
        self.createdAccount.sender_first_name(self.userStatic.first_name_user)
        self.createdAccount.sender_last_name(self.userStatic.last_name_user)
        self.createdAccount.click_in_mail_for_confirmation()
        self.createdAccount.sender_password(self.userStatic.password_user)
        self.createdAccount.select_day_month_and_year_with_value('3', '4', '1994')
        self.createdAccount.select_check_box_newsletter()
        self.createdAccount.sender_company_address_and_city('Software', 'América', 'San Martín')
        self.createdAccount.select_state_with_value('12')
        self.createdAccount.sender_postal_code('00000')
        self.createdAccount.select_country_with_value('21')
        self.createdAccount.complete_additional_information('Aditional Information, Great!')
        self.createdAccount.number_phone_mobile_and_home_phone(self.utilsFunctions.generate_number_phone(), self.
                                                               utilsFunctions.generate_number_phone())
        self.createdAccount.sender_address_aditional_alias('This is my address!')
        self.createdAccount.click_button_register()
        name_user_register = self.myAccount.return_text_user_register()
        title_register_successfully = self.myAccount.return_text_of_banner()
        self.assertEqual('Lorena Pérez', name_user_register)
        self.assertTrue('MY ACCOUNT' in title_register_successfully)

    ''' Método con las post-condiciones'''

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
