from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageBuy:
    def __init__(self, driver):
        self.driver = driver
        self.quantity_wanted = (By.ID, 'quantity_wanted')
        self.button_plus = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i')

    def push_quantity(self, quantity):
        quantity_push = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.quantity_wanted))
        quantity_push.clear()
        quantity_push.send_keys(quantity)

    def add_elements(self, quantity):
        #presiona el botón, cuantas veces le pase por parámetro
        for i in range(quantity):
            add_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_plus))
            add_element.click()

    def get_number_of_elements(self):
        #devuelvo el atributo value del elemento quantity wanted
        get_number_elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.quantity_wanted))
        get_number = get_number_elements.get_attribute('value')
        return get_number
