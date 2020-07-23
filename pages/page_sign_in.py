from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PageLogin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.box_email_adress = (By.ID, 'email_create')
        self.button_create_account = (By.XPATH, '//*[@id="SubmitCreate"]/span')
        # to user registered
        self.box_email_registered = (By.ID, 'email')
        self.box_password_registered = (By.ID, 'passwd')
        self.button_sign_in_registered = (By.XPATH, '//*[@id="SubmitLogin"]/span')

    def send_mail_box(self, text):
        sender_mail = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.box_email_adress))
        sender_mail.send_keys(text)

    def push_create_an_account(self):
        create_account = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.button_create_account))
        create_account.click()

    def push_button_sign_in_registered(self):
        sign_in_registered = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.button_sign_in_registered))
        sign_in_registered.click()

    def send_mail_user_registered(self, text):
        send_mail = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.box_email_registered))
        send_mail.send_keys(text)

    def send_password_user_registered(self, text):
        send_pass = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.box_password_registered))
        send_pass.send_keys(text)
