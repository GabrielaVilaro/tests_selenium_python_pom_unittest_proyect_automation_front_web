from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageCartSummary:
    def __init__(self, driver):
        self.driver = driver
        self.title_text_cart = (By.ID, 'cart_title')
        self.total_valor_price = (By.ID, 'total_price')

    def get_text_of_title_shopping_cart(self):
        text_title_shopping_cart = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.title_text_cart))
        text_title = text_title_shopping_cart.text
        return text_title

    def get_number_of_price_total(self):
        number_price_total = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.total_valor_price))
        number_price = number_price_total.text
        return number_price

