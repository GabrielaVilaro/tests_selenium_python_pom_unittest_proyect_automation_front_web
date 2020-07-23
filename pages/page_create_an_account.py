from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PageCreateAccount(BasePage):
    def __init__(self, driver):
        # locators datos personales
        super().__init__(driver)
        self.title_of_create_authentication = (By.XPATH, '//*[@id="noSlide"]/h1')
        self.radio_button_gender = (By.ID, 'id_gender2')
        self.first_name_box = (By.ID, 'customer_firstname')
        self.last_name_box = (By.ID, 'customer_lastname')
        self.email_box = (By.ID, 'email')
        self.password_box = (By.ID, 'passwd')
        self.select_day = (By.ID, 'days')
        self.select_month = (By.ID, 'months')
        self.select_year = (By.ID, 'years')
        self.select_checkbox = (By.ID, 'newsletter')
        # locators direccion
        self.first_name_box_adress = (By.ID, 'firstname')
        self.last_name_box_adress = (By.ID, 'lastname')
        self.company_name_box = (By.ID, 'company')
        self.address_box = (By.ID, 'address1')
        self.address_line_two_box = (By.ID, 'address2')
        self.city_name_box = (By.ID, 'city')
        self.state_select_list = (By.ID, 'id_state')
        self.postal_code_box = (By.ID, 'postcode')
        self.country_select_list = (By.ID, 'id_country')
        self.additional_information_box = (By.ID, 'other')
        self.home_phone_box = (By.ID, 'phone')
        self.mobile_phone_box = (By.ID, 'phone_mobile')
        self.alias_address_box = (By.ID, 'alias')
        # botón registrarse
        self.button_register = (By.XPATH, '//*[@id="submitAccount"]/span')

    def return_title_of_create_authentication(self):
        title_of_page_create_account_authentication = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located
            (self.title_of_create_authentication))
        title = title_of_page_create_account_authentication.text

        return title

    def select_button_radio_gender(self):
        push_radio_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.radio_button_gender))
        push_radio_button.click()

    def sender_first_name(self, first_name):
        sender_first_name = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.first_name_box))
        sender_first_name.send_keys(first_name)

    def sender_last_name(self, last_name):
        sender_last_name = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.last_name_box))
        sender_last_name.send_keys(last_name)

    def click_in_mail_for_confirmation(self):
        click_mail = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.email_box))
        click_mail.click()

    def sender_password(self, text):
        send_pass = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password_box))
        send_pass.send_keys(text)

    def select_day_month_and_year_with_value(self, day, month, year):
        # dia
        wait = WebDriverWait(self.driver, 5)
        item = wait.until(EC.presence_of_element_located(self.select_day))
        item = Select(item)
        item.select_by_value(day)
        # mes
        item = wait.until(EC.presence_of_element_located(self.select_month))
        item = Select(item)
        item.select_by_value(month)
        # año
        item = wait.until(EC.presence_of_element_located(self.select_year))
        item = Select(item)
        item.select_by_value(year)

    def select_check_box_newsletter(self):
        push_check_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.select_checkbox))
        push_check_button.click()

    def sender_company_address_and_city(self, company, address, city):
        sender_company = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.company_name_box))
        sender_company.send_keys(company)
        sender_address = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.address_box))
        sender_address.send_keys(address)
        sender_city = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.city_name_box))
        sender_city.send_keys(city)

    def select_state_with_value(self, value):
        wait = WebDriverWait(self.driver, 5)
        item = wait.until(EC.presence_of_element_located(self.state_select_list))
        item = Select(item)
        item.select_by_value(value)

    def sender_postal_code(self, text):
        sender_cp = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.postal_code_box))
        sender_cp.send_keys(text)

    def select_country_with_value(self, value):
        wait = WebDriverWait(self.driver, 5)
        item = wait.until(EC.presence_of_element_located(self.country_select_list))
        item = Select(item)
        item.select_by_value(value)

    def complete_additional_information(self, text):
        complete_information = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.additional_information_box))
        complete_information.send_keys(text)

    def number_phone_mobile_and_home_phone(self, mobile, phone):
        phone_mobile = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.mobile_phone_box))
        phone_mobile.send_keys(mobile)
        phone_home = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.home_phone_box))
        phone_home.send_keys(phone)

    def sender_address_aditional_alias(self, text):
        address_alias = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.alias_address_box))
        address_alias.send_keys(text)

    def click_button_register(self):
        push_button_register = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.button_register))
        push_button_register.click()
