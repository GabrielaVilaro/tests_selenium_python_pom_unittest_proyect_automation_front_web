from selenium.webdriver.common.by import By

class PageBuy:
    def __init__(self, driver):
        self.driver = driver
        self.quantity_wanted = (By.ID, 'quantity_wanted')
        self.button_plus = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i')


    def push_quantity(self, quantity):
        self.driver.find_element(self.quantity_wanted).clear()
        self.driver.find_element(self.quantity_wanted).send_keys(quantity)

    def add_elements(self, quantity):
        #presiona el botón, cuantas veces le pase por parámetro
        for i in range(quantity):
            self.driver.find_element(self.button_plus).click()

    def get_number_of_elements(self):
        #devuelvo el atributo value del elemento quantity wanted
        return self.driver.find_element(self.quantity_wanted).get_attribute('value')
