import random
import string

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class PageLogin:

    def __init__(self, driver):
        self.driver = driver
        self.box_email_adress = (By.ID, 'email_create')
        self.button_create_account = (By.XPATH, '//*[@id="SubmitCreate"]/span')

    def send_mail_box(self, text):
        sender_mail = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.box_email_adress))
        sender_mail.send_keys(text)

    def push_create_an_account(self):
        select_create_account = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.button_create_account))
        select_create_account.click()

