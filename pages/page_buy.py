from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageBuy:
    def __init__(self, driver):
        self.driver = driver
        self.quantity_wanted = (By.NAME, 'qty')
        self.button_plus = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i')
        self.button_add_to_cart = (By.XPATH, '//*[@id="add_to_cart"]/button/span')
        self.successfully_add_product_text = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/h2')
        self.button_proceed_to_checkout = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')

    def push_quantity(self, quantity):
        try:
            quantity_push = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.quantity_wanted))
            quantity_push.clear()
            quantity_push.send_keys(quantity)
        except:
            print('No se encontró el elemento')

    def add_elements(self, quantity):
        #presiona el botón, cuantas veces le pase por parámetro
        for i in range(quantity):
            push_click = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.button_plus))
            push_click.click()

    def get_number_of_elements(self):
        #devuelvo el atributo value del elemento quantity wanted
        get_number_elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.quantity_wanted))
        get_number = get_number_elements.get_attribute('value')
        return get_number

    def push_add_to_cart(self):
        add_to_cart = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.button_add_to_cart))
        add_to_cart.click()

    def get_text_successfully_add_product_text(self):
        text_add_product = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.successfully_add_product_text))
        text_add = text_add_product.text
        return text_add

    def push_button_proceed_to_checkout(self):
        proceed_checkout =  WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_proceed_to_checkout))
        proceed_checkout.click()

