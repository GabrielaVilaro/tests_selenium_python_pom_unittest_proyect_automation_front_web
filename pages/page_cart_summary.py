from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class PageCartSummary(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # summary
        self.title_text_cart = (By.ID, 'cart_title')
        self.total_valor_price = (By.ID, 'total_price')
        self.button_proceed_to_checkout = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')
        # address
        self.text_title_page_address = (By.XPATH, '//*[@id="center_column"]/h1')
        self.box_comment_of_address = (By.NAME, 'message')
        self.button_proceed_to_checkout_address = (By.XPATH, '//*[@id="center_column"]/form/p/button/span')
        # shipping
        self.text_title_page_shipping = (By.XPATH, '//*[@id="carrier_area"]/h1')
        self.price_of_delivery_shipping = (
            By.CLASS_NAME, 'delivery_option_price')
        self.check_box_agree_terms_and_conditions = (By.ID, 'cgv')
        self.button_proceed_to_checkout_shipping = (By.XPATH, '//*[@id="center_column"]/form/p/button/span')
        #payment
        self.text_title_page_payment = (By.XPATH, '//*[@id="center_column"]/h1')
        self.total_price_finally = (By.ID, 'total_price')
        self.button_proceed_to_checkout_payment = (By.XPATH, '//*[@id="form"]/p/button/span')

    # summary
    def get_text_of_title_shopping_cart(self):
        text_title_shopping_cart = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.title_text_cart))
        text_title = text_title_shopping_cart.text
        return text_title

    def get_number_of_price_total(self):
        number_price_total = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.total_valor_price))
        number_price = number_price_total.text
        return number_price

    def push_button_proceed_to_checkout_address(self):
        push_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.button_proceed_to_checkout))
        push_button.click()

    # address
    def get_text_of_title_address(self):
        text_title_address = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.text_title_page_address))
        text = text_title_address.text
        return text

    def send_text_in_box_comment_of_address(self, text):
        message_of_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.box_comment_of_address))
        message_of_box.send_keys(text)

    def push_button_proceed_to_checkout(self):
        push_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.button_proceed_to_checkout_address))
        push_button.click()

    # shipping
    def get_text_of_title_shipping(self):
        text_title_shipping = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.text_title_page_shipping))
        text_title = text_title_shipping.text
        return text_title

    def get_text_price_of_delivery_shipping(self):
        price_delivery = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.price_of_delivery_shipping))
        price = price_delivery.text
        return price

    def click_of_check_box_terms_and_conditions(self):
        push_check_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.check_box_agree_terms_and_conditions))
        push_check_box.click()

    def push_button_proceed_to_checkout_shipping(self):
        push_button_shipping = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.button_proceed_to_checkout_shipping))
        push_button_shipping.click()

    #payment

    def push_button_proceed_to_checkout_payment(self):
        push_button_payment = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.button_proceed_to_checkout_payment))
        push_button_payment.click()

    def get_text_of_title_payment(self):
        text_title_payment = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.text_title_page_payment))
        text_title = text_title_payment.text
        return text_title

    def get_text_price_total_finally(self):
        price_total = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.total_price_finally))
        price = price_total.text
        return price
